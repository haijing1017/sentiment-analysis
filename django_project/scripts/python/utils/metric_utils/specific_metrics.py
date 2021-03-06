import json
from base_metric import BaseMetric
from abc import ABCMeta as _ABCMeta, abstractmethod


class _SpecificMetric(BaseMetric):
    __metaclass__ = _ABCMeta

    def __init__(self):
        BaseMetric.__init__(self)
        self.db_column = ''
        self.db_column_with_spam = ''

    def get_db_column(self, consider_spam):
        return self.db_column if not consider_spam else self.db_column_with_spam

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_db_safe_stats(self):
        pass

    @abstractmethod
    def print_stats(self):
        pass

    @classmethod
    @abstractmethod
    def metric_name(cls):
        pass


class AccuracyMetric(_SpecificMetric):

    def __init__(self):
        _SpecificMetric.__init__(self)
        self.accuracy = 0
        self.db_column = 'accuracy'
        self.db_column_with_spam = 'accuracy_with_spam'

    def calculate_stats(self):
        correct_sentiment_predictions = sum(self.TP.values())
        self.accuracy = round(correct_sentiment_predictions / float(self.total_sentiment_predictions), 4)

    def get_stats(self):
        return self.accuracy

    def get_db_safe_stats(self):
        return self.accuracy

    def print_stats(self):
        print("Accuracy: %f " % self.accuracy)

    @classmethod
    def metric_name(cls):
        return "accuracy"


class RecallMetric(_SpecificMetric):

    def __init__(self):
        _SpecificMetric.__init__(self)
        self.recall = {
            'positive': 0,
            'negative': 0,
            'neutral': 0
        }
        self.db_column = 'recall'
        self.db_column_with_spam = 'recall_with_spam'

    def calculate_stats(self):
        for sentiment in self.recall.keys():
            TP = self.TP[sentiment]
            FN = self.FN[sentiment]
            self.recall[sentiment] = round(TP/float(TP+FN), 4)

    def get_stats(self):
        return self.recall

    def get_db_safe_stats(self):
        return json.dumps(self.recall)

    def print_stats(self):
        print("Recall: %s" % json.dumps(self.recall, indent=2))

    @classmethod
    def metric_name(cls):
        return "recall"


class PrecisionMetric(_SpecificMetric):

    def __init__(self):
        _SpecificMetric.__init__(self)

        self.precision = {
            'positive': 0,
            'negative': 0,
            'neutral': 0
        }

        self.db_column = 'precision'
        self.db_column_with_spam = 'precision_with_spam'

    def calculate_stats(self):
        for sentiment in self.precision.keys():
            TP = self.TP[sentiment]
            FP = self.FP[sentiment]
            self.precision[sentiment] = round(TP / float(TP + FP), 4)

    def get_stats(self):
        return self.precision

    def get_db_safe_stats(self):
        return json.dumps(self.precision)

    def print_stats(self):
        print("Precision: %s" % json.dumps(self.precision, indent=2))

    @classmethod
    def metric_name(cls):
        return "precision"


