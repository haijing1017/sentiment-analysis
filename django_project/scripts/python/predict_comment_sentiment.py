import json
from utils.print_utils.helpers import print_horizontal_rule
from utils.db_utils.base_db import Database
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.api_utils.sentiment_api import TextProcessingAPI, ViveknAPI, IndicoAPI, IndicoHqAPI
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser


def main():
    API_choices = {
        ViveknAPI.__name__: ViveknAPI,
        IndicoAPI.__name__: IndicoAPI,
        IndicoHqAPI.__name__: IndicoHqAPI,
        TextProcessingAPI.__name__: TextProcessingAPI}

    parser = IdSelectionArgumentParser(
        description=
        'Makes api calls to determine \
        the sentiment of a comment and \
        store the results in a database')

    parser.add_argument_with_choices(
        '-api',
        required=True,
        choices=API_choices.keys(),
        help='choose from the listed api options')

    parser.add_boolean_argument(
        '--original-language',
        action='store_true',
        default=False,
        help='get comment sentiment in original language')

    parser.parse_args()

    if parser.args.original_language and parser.args.api not in (ViveknAPI.__name__, TextProcessingAPI.__name__):
        print(parser.args.api + ' does not support original language sentiment analysis')
        return
    elif parser.args.original_language:
        api = API_choices.get(parser.args.api)(parser.args.original_language)
    else:
        api = API_choices.get(parser.args.api)()

    run_sentiment_api_batch(
        api=api,
        id_selection=parser.id_selection,
        original_language=parser.args.original_language)


def run_sentiment_api_batch(api=None, id_selection="", db_name="sentiment_db", original_language=False):
    """
    Open two database connections:
        - one to fetch comment records
        - another to update comment_sentiment records
    """
    db = Database(db=db_name)
    db.connect()

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    print ('\nUsing %s ' % api)

    if id_selection != '':
        id_selection = id_selection.replace('id', 'c.id') + ' AND '

    results = db.fetch_all(
        select='c.id, c.content, s.english_translation',
        from_clause=
        'im_commento AS c JOIN   \
        im_commento_sentiment AS s\
        ON c.id = s.idcommento',
        where=id_selection + "s.english_translation != ''",
        order_by='c.id ASC')

    for row in results:
        print_horizontal_rule()
        comment_id = row[0]
        content = row[1]
        english_translation = row[2]

        print ("Comment_id: %s" % comment_id)
        print ("Content: %s" % content)
        print ("Translation: %s" % english_translation)

        api.set_data(content if original_language else english_translation)
        api.post()

        if api.is_request_successful():
            api.update_sentiment_stats()
            print ("Predicted sentiment: %s" % json.dumps(api.get_sentiment_stats(), indent=2))

            db_sentiment.update(
                comment_id=comment_id,
                column=api.sentiment_api_column,
                value=json.dumps(api.get_sentiment_stats()))
        else:
            print ("API request was NOT successful: returned %d status code" % api.get_status_code())
            break

    print_horizontal_rule()
    db.close()
    db_sentiment.close()


if __name__ == '__main__':
    main()
