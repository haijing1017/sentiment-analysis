mysqldump --user=root --password=root sentiment_db im_commento_sentiment --replace --skip-add-drop-table -t --where="idcommento<'10'" > real_sentiment_dump.sql
mysqldump --user=root --password=sentiment1234 sentiment_db im_commento_sentiment --replace --skip-add-drop-table -t  > im_commento_dump.sql

