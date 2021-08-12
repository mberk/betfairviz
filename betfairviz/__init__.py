import datetime
import itertools
from enum import Enum
from typing import Any, Dict, Optional, Union

from betfairlightweight.resources.bettingresources import MarketBook
from betfairlightweight.resources.bettingresources import RunnerBook
from IPython import get_ipython
from IPython.display import HTML
from IPython.display import Pretty
from IPython.lib.pretty import pretty

from betfairutil import calculate_book_percentage
from betfairutil import calculate_total_matched
from betfairutil import get_runner_book_from_market_book
from betfairutil import is_market_book
from betfairutil import is_runner_book
from betfairutil import Side

EXAMPLE_MARKET_BOOK = {
    'betDelay': 1,
    'bspReconciled': True,
    'complete': True,
    'crossMatching': False,
    'inplay': True,
    'isMarketDataDelayed': None,
    'keyLineDescription': None,
    'lastMatchTime': None,
    'marketDefinition': {
        'betDelay': 1,
        'bettingType': 'ODDS',
        'bspMarket': True,
        'bspReconciled': True,
        'complete': True,
        'countryCode': 'GB',
        'crossMatching': False,
        'discountAllowed': True,
        'eventId': '29987033',
        'eventName': 'Sand  31st Aug',
        'eventTypeId': '7',
        'inPlay': True,
        'marketBaseRate': 5.0,
        'marketTime': '2020-08-31T18:30:00.000Z',
        'marketType': 'PLACE',
        'name': 'To Be Placed',
        'numberOfActiveRunners': 9,
        'numberOfWinners': 3,
        'openDate': '2020-08-31T14:00:00.000Z',
        'persistenceEnabled': True,
        'regulators': [
            'MR_INT'
        ],
        'runners': [
            {
                'adjustmentFactor': 27.12,
                'bsp': 2.14,
                'id': 26374770,
                'name': 'Arij',
                'sortPriority': 1,
                'status': 'ACTIVE'
            },
            {
                'adjustmentFactor': 24.68,
                'bsp': 2.17,
                'id': 28007114,
                'name': 'Kitzbuhel',
                'sortPriority': 2,
                'status': 'ACTIVE'
            },
            {
                'adjustmentFactor': 24.02,
                'bsp': 2.62,
                'id': 430775,
                'name': 'Mephisto',
                'sortPriority': 3,
                'status': 'ACTIVE'
            },
            {
                'adjustmentFactor': 22.19,
                'bsp': 1.87,
                'id': 22864389,
                'name': 'Sir Canford',
                'sortPriority': 4,
                'status': 'ACTIVE'
            },
            {
                'adjustmentFactor': 16.16,
                'bsp': 3.03,
                'id': 27388539,
                'name': 'En Famille',
                'sortPriority': 5,
                'status': 'ACTIVE'
            },
            {
                'adjustmentFactor': 15.63,
                'bsp': 6.26,
                'id': 25891932,
                'name': 'Noble Dawn',
                'sortPriority': 6,
                'status': 'ACTIVE'
            },
            {
                'adjustmentFactor': 13.07,
                'bsp': 2.45,
                'id': 21952973,
                'name': 'Twpsyn',
                'sortPriority': 7,
                'status': 'ACTIVE'
            },
            {
                'adjustmentFactor': 9.59,
                'bsp': 4.6,
                'id': 19381604,
                'name': 'Isle Of Wolves',
                'sortPriority': 8,
                'status': 'ACTIVE'
            },
            {
                'adjustmentFactor': 3.38,
                'bsp': 14.7,
                'id': 25797865,
                'name': 'Nibras Wish',
                'sortPriority': 9,
                'status': 'ACTIVE'
            }
        ],
        'runnersVoidable': False,
        'status': 'SUSPENDED',
        'suspendTime': '2020-08-31T18:30:00.000Z',
        'timezone': 'Europe/London',
        'turnInPlayEnabled': True,
        'venue': 'Sandown',
        'version': 3342028375
    },
    'marketId': '1.172557162',
    'numberOfActiveRunners': 9,
    'numberOfRunners': 9,
    'numberOfWinners': 3,
    'priceLadderDefinition': None,
    'publishTime': 1598898762900,
    'runners': [
        {
            'adjustmentFactor': 24.02,
            'ex': {
                'availableToBack': [
                    {
                        'price': 2.62,
                        'size': 27.78
                    },
                    {
                        'price': 2.6,
                        'size': 14.16
                    },
                    {
                        'price': 2.58,
                        'size': 8.7
                    },
                    {
                        'price': 2.56,
                        'size': 73.13
                    },
                    {
                        'price': 2.54,
                        'size': 83.7
                    },
                    {
                        'price': 2.52,
                        'size': 2
                    },
                    {
                        'price': 2.5,
                        'size': 54.6
                    },
                    {
                        'price': 2.48,
                        'size': 555.28
                    },
                    {
                        'price': 2.46,
                        'size': 51.98
                    },
                    {
                        'price': 2.44,
                        'size': 52.71
                    },
                    {
                        'price': 2.42,
                        'size': 110.67
                    },
                    {
                        'price': 2.4,
                        'size': 8.39
                    },
                    {
                        'price': 2.38,
                        'size': 2.96
                    },
                    {
                        'price': 2.36,
                        'size': 4.36
                    },
                    {
                        'price': 2.34,
                        'size': 8.12
                    },
                    {
                        'price': 2.32,
                        'size': 66.09
                    },
                    {
                        'price': 2.3,
                        'size': 93.86
                    },
                    {
                        'price': 2.26,
                        'size': 60.23
                    },
                    {
                        'price': 2.14,
                        'size': 14.01
                    },
                    {
                        'price': 2.12,
                        'size': 20.12
                    },
                    {
                        'price': 2.08,
                        'size': 2
                    },
                    {
                        'price': 2.06,
                        'size': 695.09
                    },
                    {
                        'price': 2.04,
                        'size': 2.44
                    },
                    {
                        'price': 1.99,
                        'size': 3.95
                    },
                    {
                        'price': 1.95,
                        'size': 157.89
                    },
                    {
                        'price': 1.93,
                        'size': 777.7
                    },
                    {
                        'price': 1.92,
                        'size': 51.77
                    },
                    {
                        'price': 1.9,
                        'size': 171.67
                    },
                    {
                        'price': 1.85,
                        'size': 56.04
                    },
                    {
                        'price': 1.84,
                        'size': 357.14
                    },
                    {
                        'price': 1.61,
                        'size': 44.11
                    },
                    {
                        'price': 1.52,
                        'size': 247
                    },
                    {
                        'price': 1.45,
                        'size': 73.27
                    },
                    {
                        'price': 1.42,
                        'size': 264
                    },
                    {
                        'price': 1.39,
                        'size': 20.6
                    },
                    {
                        'price': 1.3,
                        'size': 2
                    },
                    {
                        'price': 1.29,
                        'size': 115.88
                    },
                    {
                        'price': 1.28,
                        'size': 103.57
                    },
                    {
                        'price': 1.26,
                        'size': 153.85
                    },
                    {
                        'price': 1.23,
                        'size': 500
                    },
                    {
                        'price': 1.15,
                        'size': 123.36
                    },
                    {
                        'price': 1.13,
                        'size': 2
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.06,
                        'size': 198.71
                    },
                    {
                        'price': 1.04,
                        'size': 27.77
                    },
                    {
                        'price': 1.03,
                        'size': 275.24
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 4319.84
                    }
                ],
                'availableToLay': [
                    {
                        'price': 2.66,
                        'size': 84.1
                    },
                    {
                        'price': 2.68,
                        'size': 27.67
                    },
                    {
                        'price': 2.7,
                        'size': 5.94
                    },
                    {
                        'price': 2.74,
                        'size': 7.88
                    },
                    {
                        'price': 2.88,
                        'size': 4.26
                    },
                    {
                        'price': 2.9,
                        'size': 43
                    },
                    {
                        'price': 3.05,
                        'size': 4.36
                    },
                    {
                        'price': 3.15,
                        'size': 123.36
                    },
                    {
                        'price': 4.6,
                        'size': 4.49
                    },
                    {
                        'price': 14.5,
                        'size': 10
                    },
                    {
                        'price': 80,
                        'size': 42.86
                    },
                    {
                        'price': 90,
                        'size': 2
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    },
                    {
                        'price': 1000,
                        'size': 37.77
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 1.88,
                        'size': 3.57
                    },
                    {
                        'price': 2,
                        'size': 1.18
                    },
                    {
                        'price': 2.02,
                        'size': 42.82
                    },
                    {
                        'price': 2.04,
                        'size': 4
                    },
                    {
                        'price': 2.06,
                        'size': 83.99
                    },
                    {
                        'price': 2.08,
                        'size': 112.72
                    },
                    {
                        'price': 2.1,
                        'size': 141.49
                    },
                    {
                        'price': 2.12,
                        'size': 53.01
                    },
                    {
                        'price': 2.14,
                        'size': 57.82
                    },
                    {
                        'price': 2.16,
                        'size': 134.26
                    },
                    {
                        'price': 2.18,
                        'size': 124.85
                    },
                    {
                        'price': 2.2,
                        'size': 98.74
                    },
                    {
                        'price': 2.22,
                        'size': 24.12
                    },
                    {
                        'price': 2.24,
                        'size': 3.02
                    },
                    {
                        'price': 2.26,
                        'size': 198.37
                    },
                    {
                        'price': 2.28,
                        'size': 305.9
                    },
                    {
                        'price': 2.3,
                        'size': 140.94
                    },
                    {
                        'price': 2.32,
                        'size': 12.7
                    },
                    {
                        'price': 2.34,
                        'size': 32.51
                    },
                    {
                        'price': 2.38,
                        'size': 109.45
                    },
                    {
                        'price': 2.4,
                        'size': 163.59
                    },
                    {
                        'price': 2.42,
                        'size': 152.86
                    },
                    {
                        'price': 2.44,
                        'size': 508.39
                    },
                    {
                        'price': 2.46,
                        'size': 248.07
                    },
                    {
                        'price': 2.48,
                        'size': 214.7
                    },
                    {
                        'price': 2.5,
                        'size': 194.37
                    },
                    {
                        'price': 2.52,
                        'size': 142.93
                    },
                    {
                        'price': 2.54,
                        'size': 125.8
                    },
                    {
                        'price': 2.56,
                        'size': 89.51
                    },
                    {
                        'price': 2.58,
                        'size': 52.79
                    },
                    {
                        'price': 2.6,
                        'size': 74.68
                    },
                    {
                        'price': 2.62,
                        'size': 76.6
                    },
                    {
                        'price': 2.64,
                        'size': 23.66
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 2.62,
            'removalDate': None,
            'selectionId': 430775,
            'sp': {
                'actualSP': 2.62,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 92.55
                    },
                    {
                        'price': 2.46,
                        'size': 4.77
                    },
                    {
                        'price': 2.52,
                        'size': 14.67
                    },
                    {
                        'price': 2.56,
                        'size': 2
                    },
                    {
                        'price': 2.6,
                        'size': 14.27
                    },
                    {
                        'price': 2.62,
                        'size': 7.86
                    },
                    {
                        'price': 2.66,
                        'size': 10.12
                    },
                    {
                        'price': 2.68,
                        'size': 9.04
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 2.65,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 168.54
                    },
                    {
                        'price': 32,
                        'size': 30
                    },
                    {
                        'price': 5,
                        'size': 27.01
                    },
                    {
                        'price': 2.48,
                        'size': 32.01
                    },
                    {
                        'price': 2.32,
                        'size': 63.23
                    },
                    {
                        'price': 2.3,
                        'size': 60.2
                    },
                    {
                        'price': 2.2,
                        'size': 17.15
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 2.59
            },
            'status': 'ACTIVE',
            'totalMatched': 76.6
        },
        {
            'adjustmentFactor': 24.68,
            'ex': {
                'availableToBack': [
                    {
                        'price': 2.16,
                        'size': 69.5
                    },
                    {
                        'price': 2.14,
                        'size': 85.78
                    },
                    {
                        'price': 2.12,
                        'size': 81.68
                    },
                    {
                        'price': 2.1,
                        'size': 76.39
                    },
                    {
                        'price': 2.08,
                        'size': 91.75
                    },
                    {
                        'price': 2.06,
                        'size': 75.89
                    },
                    {
                        'price': 2.04,
                        'size': 689.01
                    },
                    {
                        'price': 2.02,
                        'size': 84.21
                    },
                    {
                        'price': 2,
                        'size': 95.4
                    },
                    {
                        'price': 1.99,
                        'size': 17.76
                    },
                    {
                        'price': 1.98,
                        'size': 2.9
                    },
                    {
                        'price': 1.97,
                        'size': 3.41
                    },
                    {
                        'price': 1.96,
                        'size': 14.63
                    },
                    {
                        'price': 1.9,
                        'size': 44.05
                    },
                    {
                        'price': 1.78,
                        'size': 14.78
                    },
                    {
                        'price': 1.74,
                        'size': 977.38
                    },
                    {
                        'price': 1.69,
                        'size': 434.78
                    },
                    {
                        'price': 1.66,
                        'size': 72.17
                    },
                    {
                        'price': 1.65,
                        'size': 1112.71
                    },
                    {
                        'price': 1.61,
                        'size': 245.9
                    },
                    {
                        'price': 1.58,
                        'size': 258.62
                    },
                    {
                        'price': 1.54,
                        'size': 244
                    },
                    {
                        'price': 1.53,
                        'size': 89.87
                    },
                    {
                        'price': 1.44,
                        'size': 14.28
                    },
                    {
                        'price': 1.42,
                        'size': 264
                    },
                    {
                        'price': 1.41,
                        'size': 68.78
                    },
                    {
                        'price': 1.3,
                        'size': 99.19
                    },
                    {
                        'price': 1.23,
                        'size': 500
                    },
                    {
                        'price': 1.19,
                        'size': 210.53
                    },
                    {
                        'price': 1.16,
                        'size': 115.88
                    },
                    {
                        'price': 1.13,
                        'size': 2
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.06,
                        'size': 305.1
                    },
                    {
                        'price': 1.04,
                        'size': 27.77
                    },
                    {
                        'price': 1.03,
                        'size': 305.15
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 2616.07
                    }
                ],
                'availableToLay': [
                    {
                        'price': 2.22,
                        'size': 17.99
                    },
                    {
                        'price': 2.24,
                        'size': 46.75
                    },
                    {
                        'price': 2.26,
                        'size': 25.4
                    },
                    {
                        'price': 2.3,
                        'size': 2
                    },
                    {
                        'price': 2.34,
                        'size': 17.07
                    },
                    {
                        'price': 2.38,
                        'size': 58.85
                    },
                    {
                        'price': 2.46,
                        'size': 51
                    },
                    {
                        'price': 2.5,
                        'size': 3.04
                    },
                    {
                        'price': 2.54,
                        'size': 3.04
                    },
                    {
                        'price': 3.3,
                        'size': 114
                    },
                    {
                        'price': 4.3,
                        'size': 10
                    },
                    {
                        'price': 4.5,
                        'size': 5.53
                    },
                    {
                        'price': 13,
                        'size': 10
                    },
                    {
                        'price': 22,
                        'size': 1
                    },
                    {
                        'price': 60,
                        'size': 2
                    },
                    {
                        'price': 80,
                        'size': 40.18
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    },
                    {
                        'price': 1000,
                        'size': 75.03
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 1.66,
                        'size': 57.76
                    },
                    {
                        'price': 1.67,
                        'size': 300.47
                    },
                    {
                        'price': 1.68,
                        'size': 168.5
                    },
                    {
                        'price': 1.69,
                        'size': 74.15
                    },
                    {
                        'price': 1.7,
                        'size': 122.14
                    },
                    {
                        'price': 1.71,
                        'size': 42.01
                    },
                    {
                        'price': 1.72,
                        'size': 71.68
                    },
                    {
                        'price': 1.73,
                        'size': 51.26
                    },
                    {
                        'price': 1.74,
                        'size': 31.28
                    },
                    {
                        'price': 1.75,
                        'size': 212.48
                    },
                    {
                        'price': 1.76,
                        'size': 30.08
                    },
                    {
                        'price': 1.77,
                        'size': 168.16
                    },
                    {
                        'price': 1.78,
                        'size': 108.45
                    },
                    {
                        'price': 1.79,
                        'size': 115.4
                    },
                    {
                        'price': 1.8,
                        'size': 38.28
                    },
                    {
                        'price': 1.81,
                        'size': 30.7
                    },
                    {
                        'price': 1.82,
                        'size': 40.84
                    },
                    {
                        'price': 1.83,
                        'size': 13.24
                    },
                    {
                        'price': 1.84,
                        'size': 133.21
                    },
                    {
                        'price': 1.85,
                        'size': 46.39
                    },
                    {
                        'price': 1.86,
                        'size': 48.42
                    },
                    {
                        'price': 1.87,
                        'size': 204.24
                    },
                    {
                        'price': 1.88,
                        'size': 229.91
                    },
                    {
                        'price': 1.89,
                        'size': 74.6
                    },
                    {
                        'price': 1.9,
                        'size': 53.36
                    },
                    {
                        'price': 1.91,
                        'size': 90.38
                    },
                    {
                        'price': 1.92,
                        'size': 27.32
                    },
                    {
                        'price': 1.93,
                        'size': 33.65
                    },
                    {
                        'price': 1.94,
                        'size': 32.35
                    },
                    {
                        'price': 1.96,
                        'size': 22.54
                    },
                    {
                        'price': 1.97,
                        'size': 53.45
                    },
                    {
                        'price': 1.98,
                        'size': 14.34
                    },
                    {
                        'price': 1.99,
                        'size': 48.45
                    },
                    {
                        'price': 2,
                        'size': 47.05
                    },
                    {
                        'price': 2.02,
                        'size': 589.86
                    },
                    {
                        'price': 2.04,
                        'size': 597.81
                    },
                    {
                        'price': 2.06,
                        'size': 1186.22
                    },
                    {
                        'price': 2.08,
                        'size': 502.49
                    },
                    {
                        'price': 2.1,
                        'size': 678.06
                    },
                    {
                        'price': 2.12,
                        'size': 414.05
                    },
                    {
                        'price': 2.14,
                        'size': 386.71
                    },
                    {
                        'price': 2.16,
                        'size': 182
                    },
                    {
                        'price': 2.18,
                        'size': 219.41
                    },
                    {
                        'price': 2.2,
                        'size': 68.01
                    },
                    {
                        'price': 2.22,
                        'size': 298.55
                    },
                    {
                        'price': 2.24,
                        'size': 42.75
                    },
                    {
                        'price': 2.26,
                        'size': 16.19
                    },
                    {
                        'price': 2.28,
                        'size': 37.05
                    },
                    {
                        'price': 2.32,
                        'size': 13.84
                    },
                    {
                        'price': 2.34,
                        'size': 93.33
                    },
                    {
                        'price': 2.36,
                        'size': 144.97
                    },
                    {
                        'price': 2.38,
                        'size': 19.43
                    },
                    {
                        'price': 2.4,
                        'size': 35.28
                    },
                    {
                        'price': 2.42,
                        'size': 119.21
                    },
                    {
                        'price': 2.44,
                        'size': 21.62
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 2.16,
            'removalDate': None,
            'selectionId': 28007114,
            'sp': {
                'actualSP': 2.17,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 176.27
                    },
                    {
                        'price': 1.3,
                        'size': 6
                    },
                    {
                        'price': 2.04,
                        'size': 21.36
                    },
                    {
                        'price': 2.08,
                        'size': 6.65
                    },
                    {
                        'price': 2.14,
                        'size': 6.99
                    },
                    {
                        'price': 2.18,
                        'size': 8.04
                    },
                    {
                        'price': 2.28,
                        'size': 22.47
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 2.23,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 254.78
                    },
                    {
                        'price': 5,
                        'size': 23.95
                    },
                    {
                        'price': 2.02,
                        'size': 32.01
                    },
                    {
                        'price': 1.95,
                        'size': 54.41
                    },
                    {
                        'price': 1.9,
                        'size': 68.46
                    },
                    {
                        'price': 1.84,
                        'size': 16.62
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 2.18
            },
            'status': 'ACTIVE',
            'totalMatched': 401.4
        },
        {
            'adjustmentFactor': 27.12,
            'ex': {
                'availableToBack': [
                    {
                        'price': 2.12,
                        'size': 76.68
                    },
                    {
                        'price': 2.1,
                        'size': 99.03
                    },
                    {
                        'price': 2.08,
                        'size': 188.45
                    },
                    {
                        'price': 2.06,
                        'size': 78.05
                    },
                    {
                        'price': 2.04,
                        'size': 691.89
                    },
                    {
                        'price': 2.02,
                        'size': 99.52
                    },
                    {
                        'price': 2,
                        'size': 100.64
                    },
                    {
                        'price': 1.99,
                        'size': 99.52
                    },
                    {
                        'price': 1.98,
                        'size': 4.62
                    },
                    {
                        'price': 1.97,
                        'size': 87.64
                    },
                    {
                        'price': 1.96,
                        'size': 83.78
                    },
                    {
                        'price': 1.95,
                        'size': 84.65
                    },
                    {
                        'price': 1.92,
                        'size': 45.92
                    },
                    {
                        'price': 1.91,
                        'size': 83.4
                    },
                    {
                        'price': 1.9,
                        'size': 86.67
                    },
                    {
                        'price': 1.87,
                        'size': 9.63
                    },
                    {
                        'price': 1.84,
                        'size': 5.43
                    },
                    {
                        'price': 1.82,
                        'size': 2
                    },
                    {
                        'price': 1.81,
                        'size': 16.57
                    },
                    {
                        'price': 1.78,
                        'size': 15.46
                    },
                    {
                        'price': 1.77,
                        'size': 954.16
                    },
                    {
                        'price': 1.7,
                        'size': 214.29
                    },
                    {
                        'price': 1.68,
                        'size': 1063.62
                    },
                    {
                        'price': 1.67,
                        'size': 71.09
                    },
                    {
                        'price': 1.66,
                        'size': 227.27
                    },
                    {
                        'price': 1.57,
                        'size': 263.16
                    },
                    {
                        'price': 1.55,
                        'size': 86.6
                    },
                    {
                        'price': 1.54,
                        'size': 277.78
                    },
                    {
                        'price': 1.51,
                        'size': 2.55
                    },
                    {
                        'price': 1.47,
                        'size': 45.09
                    },
                    {
                        'price': 1.45,
                        'size': 74.76
                    },
                    {
                        'price': 1.43,
                        'size': 262
                    },
                    {
                        'price': 1.34,
                        'size': 280
                    },
                    {
                        'price': 1.33,
                        'size': 2.55
                    },
                    {
                        'price': 1.3,
                        'size': 2
                    },
                    {
                        'price': 1.28,
                        'size': 111.4
                    },
                    {
                        'price': 1.23,
                        'size': 673.91
                    },
                    {
                        'price': 1.21,
                        'size': 62.61
                    },
                    {
                        'price': 1.14,
                        'size': 149.14
                    },
                    {
                        'price': 1.13,
                        'size': 2
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.08,
                        'size': 122.75
                    },
                    {
                        'price': 1.06,
                        'size': 171.71
                    },
                    {
                        'price': 1.04,
                        'size': 27.77
                    },
                    {
                        'price': 1.03,
                        'size': 298.42
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 4000.12
                    }
                ],
                'availableToLay': [
                    {
                        'price': 2.2,
                        'size': 4.25
                    },
                    {
                        'price': 2.22,
                        'size': 41.85
                    },
                    {
                        'price': 2.24,
                        'size': 148.48
                    },
                    {
                        'price': 2.26,
                        'size': 33.27
                    },
                    {
                        'price': 2.44,
                        'size': 51
                    },
                    {
                        'price': 2.48,
                        'size': 22.85
                    },
                    {
                        'price': 2.56,
                        'size': 22.86
                    },
                    {
                        'price': 2.78,
                        'size': 135
                    },
                    {
                        'price': 4,
                        'size': 6.17
                    },
                    {
                        'price': 11.5,
                        'size': 10
                    },
                    {
                        'price': 22,
                        'size': 1
                    },
                    {
                        'price': 85,
                        'size': 43.75
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    },
                    {
                        'price': 1000,
                        'size': 4
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 1.78,
                        'size': 23.16
                    },
                    {
                        'price': 1.79,
                        'size': 329.33
                    },
                    {
                        'price': 1.8,
                        'size': 170.04
                    },
                    {
                        'price': 1.81,
                        'size': 224.61
                    },
                    {
                        'price': 1.82,
                        'size': 821.91
                    },
                    {
                        'price': 1.83,
                        'size': 654.6
                    },
                    {
                        'price': 1.84,
                        'size': 278.16
                    },
                    {
                        'price': 1.85,
                        'size': 283.32
                    },
                    {
                        'price': 1.86,
                        'size': 785.48
                    },
                    {
                        'price': 1.87,
                        'size': 155.15
                    },
                    {
                        'price': 1.88,
                        'size': 138.1
                    },
                    {
                        'price': 1.89,
                        'size': 205.77
                    },
                    {
                        'price': 1.9,
                        'size': 664.31
                    },
                    {
                        'price': 1.91,
                        'size': 17.5
                    },
                    {
                        'price': 1.92,
                        'size': 9.99
                    },
                    {
                        'price': 1.93,
                        'size': 99.03
                    },
                    {
                        'price': 1.94,
                        'size': 21.14
                    },
                    {
                        'price': 1.95,
                        'size': 125.75
                    },
                    {
                        'price': 1.96,
                        'size': 227.14
                    },
                    {
                        'price': 1.97,
                        'size': 102.86
                    },
                    {
                        'price': 1.98,
                        'size': 403.49
                    },
                    {
                        'price': 1.99,
                        'size': 89.02
                    },
                    {
                        'price': 2,
                        'size': 826.27
                    },
                    {
                        'price': 2.02,
                        'size': 687.42
                    },
                    {
                        'price': 2.04,
                        'size': 448.61
                    },
                    {
                        'price': 2.06,
                        'size': 549.48
                    },
                    {
                        'price': 2.08,
                        'size': 593.56
                    },
                    {
                        'price': 2.1,
                        'size': 357.68
                    },
                    {
                        'price': 2.12,
                        'size': 956.8
                    },
                    {
                        'price': 2.14,
                        'size': 841.8
                    },
                    {
                        'price': 2.16,
                        'size': 675.38
                    },
                    {
                        'price': 2.18,
                        'size': 195.55
                    },
                    {
                        'price': 2.2,
                        'size': 67.35
                    },
                    {
                        'price': 2.22,
                        'size': 53.88
                    },
                    {
                        'price': 2.24,
                        'size': 78.61
                    },
                    {
                        'price': 2.28,
                        'size': 0.03
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 2.12,
            'removalDate': None,
            'selectionId': 26374770,
            'sp': {
                'actualSP': 2.14,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 306.06
                    },
                    {
                        'price': 1.11,
                        'size': 5
                    },
                    {
                        'price': 1.15,
                        'size': 10
                    },
                    {
                        'price': 1.5,
                        'size': 50
                    },
                    {
                        'price': 2,
                        'size': 4.24
                    },
                    {
                        'price': 2.02,
                        'size': 10
                    },
                    {
                        'price': 2.1,
                        'size': 20.18
                    },
                    {
                        'price': 2.12,
                        'size': 2.36
                    },
                    {
                        'price': 2.18,
                        'size': 12.68
                    },
                    {
                        'price': 2.2,
                        'size': 6.99
                    },
                    {
                        'price': 2.22,
                        'size': 9.78
                    },
                    {
                        'price': 2.24,
                        'size': 8.04
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 2.02,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 339.1
                    },
                    {
                        'price': 5,
                        'size': 23.66
                    },
                    {
                        'price': 2.08,
                        'size': 22
                    },
                    {
                        'price': 2.06,
                        'size': 10.01
                    },
                    {
                        'price': 1.97,
                        'size': 54.42
                    },
                    {
                        'price': 1.92,
                        'size': 51.83
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 2.11
            },
            'status': 'ACTIVE',
            'totalMatched': 2473.98
        },
        {
            'adjustmentFactor': 22.19,
            'ex': {
                'availableToBack': [
                    {
                        'price': 1.84,
                        'size': 54.02
                    },
                    {
                        'price': 1.83,
                        'size': 36.12
                    },
                    {
                        'price': 1.82,
                        'size': 26.7
                    },
                    {
                        'price': 1.81,
                        'size': 93.7
                    },
                    {
                        'price': 1.8,
                        'size': 94.87
                    },
                    {
                        'price': 1.79,
                        'size': 280.43
                    },
                    {
                        'price': 1.78,
                        'size': 702
                    },
                    {
                        'price': 1.77,
                        'size': 19.63
                    },
                    {
                        'price': 1.75,
                        'size': 2.95
                    },
                    {
                        'price': 1.73,
                        'size': 18.15
                    },
                    {
                        'price': 1.72,
                        'size': 1004.53
                    },
                    {
                        'price': 1.64,
                        'size': 1130.09
                    },
                    {
                        'price': 1.62,
                        'size': 241.94
                    },
                    {
                        'price': 1.61,
                        'size': 273.3
                    },
                    {
                        'price': 1.6,
                        'size': 79.38
                    },
                    {
                        'price': 1.58,
                        'size': 258.62
                    },
                    {
                        'price': 1.49,
                        'size': 252
                    },
                    {
                        'price': 1.46,
                        'size': 103.54
                    },
                    {
                        'price': 1.45,
                        'size': 333.33
                    },
                    {
                        'price': 1.44,
                        'size': 14.28
                    },
                    {
                        'price': 1.43,
                        'size': 348.84
                    },
                    {
                        'price': 1.42,
                        'size': 63.55
                    },
                    {
                        'price': 1.3,
                        'size': 130.93
                    },
                    {
                        'price': 1.29,
                        'size': 137.93
                    },
                    {
                        'price': 1.23,
                        'size': 500
                    },
                    {
                        'price': 1.15,
                        'size': 146.54
                    },
                    {
                        'price': 1.13,
                        'size': 2
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.06,
                        'size': 2
                    },
                    {
                        'price': 1.05,
                        'size': 152.52
                    },
                    {
                        'price': 1.04,
                        'size': 155.24
                    },
                    {
                        'price': 1.03,
                        'size': 293.93
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 3933.62
                    }
                ],
                'availableToLay': [
                    {
                        'price': 1.88,
                        'size': 0.41
                    },
                    {
                        'price': 1.89,
                        'size': 47.86
                    },
                    {
                        'price': 1.91,
                        'size': 6.16
                    },
                    {
                        'price': 1.92,
                        'size': 105.86
                    },
                    {
                        'price': 1.93,
                        'size': 11.89
                    },
                    {
                        'price': 1.94,
                        'size': 4.91
                    },
                    {
                        'price': 1.95,
                        'size': 4.83
                    },
                    {
                        'price': 1.97,
                        'size': 2.56
                    },
                    {
                        'price': 1.99,
                        'size': 63
                    },
                    {
                        'price': 2.02,
                        'size': 2
                    },
                    {
                        'price': 2.04,
                        'size': 4.58
                    },
                    {
                        'price': 2.06,
                        'size': 9.04
                    },
                    {
                        'price': 2.08,
                        'size': 2.95
                    },
                    {
                        'price': 2.1,
                        'size': 2.95
                    },
                    {
                        'price': 2.16,
                        'size': 23.1
                    },
                    {
                        'price': 2.38,
                        'size': 10.45
                    },
                    {
                        'price': 2.4,
                        'size': 16.34
                    },
                    {
                        'price': 3.55,
                        'size': 106
                    },
                    {
                        'price': 4,
                        'size': 2
                    },
                    {
                        'price': 4.5,
                        'size': 5.53
                    },
                    {
                        'price': 15.5,
                        'size': 10
                    },
                    {
                        'price': 22,
                        'size': 1.64
                    },
                    {
                        'price': 95,
                        'size': 45.53
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    },
                    {
                        'price': 1000,
                        'size': 4
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 1.84,
                        'size': 7.58
                    },
                    {
                        'price': 1.85,
                        'size': 53.73
                    },
                    {
                        'price': 1.86,
                        'size': 102.88
                    },
                    {
                        'price': 1.87,
                        'size': 101.76
                    },
                    {
                        'price': 1.88,
                        'size': 131.73
                    },
                    {
                        'price': 1.89,
                        'size': 39.35
                    },
                    {
                        'price': 1.9,
                        'size': 397.13
                    },
                    {
                        'price': 1.91,
                        'size': 422.82
                    },
                    {
                        'price': 1.92,
                        'size': 188.21
                    },
                    {
                        'price': 1.93,
                        'size': 187.73
                    },
                    {
                        'price': 1.94,
                        'size': 181.01
                    },
                    {
                        'price': 1.95,
                        'size': 91.97
                    },
                    {
                        'price': 1.96,
                        'size': 97.7
                    },
                    {
                        'price': 1.97,
                        'size': 73.74
                    },
                    {
                        'price': 1.98,
                        'size': 182.25
                    },
                    {
                        'price': 1.99,
                        'size': 468.15
                    },
                    {
                        'price': 2,
                        'size': 512.16
                    },
                    {
                        'price': 2.02,
                        'size': 429.17
                    },
                    {
                        'price': 2.04,
                        'size': 620.81
                    },
                    {
                        'price': 2.06,
                        'size': 154.02
                    },
                    {
                        'price': 2.08,
                        'size': 187.86
                    },
                    {
                        'price': 2.1,
                        'size': 82.48
                    },
                    {
                        'price': 2.12,
                        'size': 14.07
                    },
                    {
                        'price': 2.14,
                        'size': 34.55
                    },
                    {
                        'price': 2.16,
                        'size': 167.78
                    },
                    {
                        'price': 2.18,
                        'size': 272.04
                    },
                    {
                        'price': 2.2,
                        'size': 275.95
                    },
                    {
                        'price': 2.22,
                        'size': 592.47
                    },
                    {
                        'price': 2.24,
                        'size': 406.13
                    },
                    {
                        'price': 2.26,
                        'size': 212.34
                    },
                    {
                        'price': 2.28,
                        'size': 325.49
                    },
                    {
                        'price': 2.3,
                        'size': 210.6
                    },
                    {
                        'price': 2.32,
                        'size': 116.01
                    },
                    {
                        'price': 2.34,
                        'size': 45.11
                    },
                    {
                        'price': 2.36,
                        'size': 35.72
                    },
                    {
                        'price': 2.38,
                        'size': 87.98
                    },
                    {
                        'price': 2.4,
                        'size': 21.71
                    },
                    {
                        'price': 2.42,
                        'size': 17.96
                    },
                    {
                        'price': 2.5,
                        'size': 9.69
                    },
                    {
                        'price': 2.62,
                        'size': 16.12
                    },
                    {
                        'price': 2.76,
                        'size': 4
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 1.88,
            'removalDate': None,
            'selectionId': 22864389,
            'sp': {
                'actualSP': 1.87,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 219.95
                    },
                    {
                        'price': 1.1,
                        'size': 4.31
                    },
                    {
                        'price': 1.15,
                        'size': 7.13
                    },
                    {
                        'price': 1.9,
                        'size': 2.99
                    },
                    {
                        'price': 1.99,
                        'size': 22.22
                    },
                    {
                        'price': 2.02,
                        'size': 12.68
                    },
                    {
                        'price': 2.06,
                        'size': 2.44
                    },
                    {
                        'price': 2.08,
                        'size': 6.99
                    },
                    {
                        'price': 2.12,
                        'size': 8.04
                    },
                    {
                        'price': 2.2,
                        'size': 4.24
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 1.92,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 133.2
                    },
                    {
                        'price': 5,
                        'size': 25.85
                    },
                    {
                        'price': 2,
                        'size': 20
                    },
                    {
                        'price': 1.99,
                        'size': 16.62
                    },
                    {
                        'price': 1.98,
                        'size': 22
                    },
                    {
                        'price': 1.92,
                        'size': 16.62
                    },
                    {
                        'price': 1.87,
                        'size': 54.39
                    },
                    {
                        'price': 1.86,
                        'size': 51.83
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 1.87
            },
            'status': 'ACTIVE',
            'totalMatched': 233.49
        },
        {
            'adjustmentFactor': 15.63,
            'ex': {
                'availableToBack': [
                    {
                        'price': 6,
                        'size': 12.84
                    },
                    {
                        'price': 5.9,
                        'size': 15.05
                    },
                    {
                        'price': 5.8,
                        'size': 44.2
                    },
                    {
                        'price': 5.7,
                        'size': 46.95
                    },
                    {
                        'price': 5.6,
                        'size': 28.31
                    },
                    {
                        'price': 5.5,
                        'size': 16.86
                    },
                    {
                        'price': 5.4,
                        'size': 19.5
                    },
                    {
                        'price': 5.3,
                        'size': 255.9
                    },
                    {
                        'price': 5.2,
                        'size': 20.24
                    },
                    {
                        'price': 5.1,
                        'size': 18.51
                    },
                    {
                        'price': 4.9,
                        'size': 19.45
                    },
                    {
                        'price': 4.8,
                        'size': 32.5
                    },
                    {
                        'price': 4.7,
                        'size': 22.99
                    },
                    {
                        'price': 4.4,
                        'size': 59.18
                    },
                    {
                        'price': 4.3,
                        'size': 224.52
                    },
                    {
                        'price': 4.2,
                        'size': 2.94
                    },
                    {
                        'price': 4.1,
                        'size': 56.23
                    },
                    {
                        'price': 3.85,
                        'size': 52.63
                    },
                    {
                        'price': 3.8,
                        'size': 265.23
                    },
                    {
                        'price': 3.75,
                        'size': 17.32
                    },
                    {
                        'price': 3.55,
                        'size': 58.82
                    },
                    {
                        'price': 3.4,
                        'size': 2.85
                    },
                    {
                        'price': 3.35,
                        'size': 2.86
                    },
                    {
                        'price': 3.25,
                        'size': 42.79
                    },
                    {
                        'price': 2.58,
                        'size': 102.77
                    },
                    {
                        'price': 2.38,
                        'size': 4.19
                    },
                    {
                        'price': 2.36,
                        'size': 159
                    },
                    {
                        'price': 2.08,
                        'size': 180
                    },
                    {
                        'price': 1.64,
                        'size': 42.61
                    },
                    {
                        'price': 1.57,
                        'size': 70.18
                    },
                    {
                        'price': 1.5,
                        'size': 11
                    },
                    {
                        'price': 1.44,
                        'size': 66.54
                    },
                    {
                        'price': 1.41,
                        'size': 5.18
                    },
                    {
                        'price': 1.3,
                        'size': 2
                    },
                    {
                        'price': 1.28,
                        'size': 106.16
                    },
                    {
                        'price': 1.23,
                        'size': 500
                    },
                    {
                        'price': 1.21,
                        'size': 2
                    },
                    {
                        'price': 1.18,
                        'size': 7.26
                    },
                    {
                        'price': 1.16,
                        'size': 145.04
                    },
                    {
                        'price': 1.13,
                        'size': 2
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.11,
                        'size': 20
                    },
                    {
                        'price': 1.06,
                        'size': 19.28
                    },
                    {
                        'price': 1.05,
                        'size': 155.51
                    },
                    {
                        'price': 1.04,
                        'size': 27.77
                    },
                    {
                        'price': 1.03,
                        'size': 284.96
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 5106.13
                    }
                ],
                'availableToLay': [
                    {
                        'price': 6.4,
                        'size': 56.92
                    },
                    {
                        'price': 6.6,
                        'size': 5.91
                    },
                    {
                        'price': 6.8,
                        'size': 2.7
                    },
                    {
                        'price': 7,
                        'size': 5.52
                    },
                    {
                        'price': 7.2,
                        'size': 4.05
                    },
                    {
                        'price': 7.4,
                        'size': 16.92
                    },
                    {
                        'price': 7.6,
                        'size': 2.25
                    },
                    {
                        'price': 7.8,
                        'size': 3.17
                    },
                    {
                        'price': 8,
                        'size': 2.25
                    },
                    {
                        'price': 8.6,
                        'size': 15
                    },
                    {
                        'price': 9,
                        'size': 7.36
                    },
                    {
                        'price': 34,
                        'size': 10
                    },
                    {
                        'price': 90,
                        'size': 48.21
                    },
                    {
                        'price': 120,
                        'size': 2
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    },
                    {
                        'price': 1000,
                        'size': 2
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 2.9,
                        'size': 8.28
                    },
                    {
                        'price': 2.92,
                        'size': 16.44
                    },
                    {
                        'price': 3,
                        'size': 20
                    },
                    {
                        'price': 3.05,
                        'size': 4
                    },
                    {
                        'price': 3.1,
                        'size': 24
                    },
                    {
                        'price': 3.15,
                        'size': 31.34
                    },
                    {
                        'price': 3.2,
                        'size': 4
                    },
                    {
                        'price': 3.35,
                        'size': 30.34
                    },
                    {
                        'price': 3.4,
                        'size': 97.84
                    },
                    {
                        'price': 3.45,
                        'size': 82.2
                    },
                    {
                        'price': 3.5,
                        'size': 431.17
                    },
                    {
                        'price': 3.55,
                        'size': 59.51
                    },
                    {
                        'price': 3.6,
                        'size': 301.12
                    },
                    {
                        'price': 3.65,
                        'size': 212.98
                    },
                    {
                        'price': 3.7,
                        'size': 68.85
                    },
                    {
                        'price': 3.75,
                        'size': 148.34
                    },
                    {
                        'price': 3.8,
                        'size': 63.14
                    },
                    {
                        'price': 3.85,
                        'size': 42.9
                    },
                    {
                        'price': 3.9,
                        'size': 67.55
                    },
                    {
                        'price': 3.95,
                        'size': 8.67
                    },
                    {
                        'price': 4,
                        'size': 110.95
                    },
                    {
                        'price': 4.1,
                        'size': 4
                    },
                    {
                        'price': 4.2,
                        'size': 68.77
                    },
                    {
                        'price': 4.3,
                        'size': 89.94
                    },
                    {
                        'price': 4.4,
                        'size': 48.48
                    },
                    {
                        'price': 4.5,
                        'size': 66.16
                    },
                    {
                        'price': 4.6,
                        'size': 68.45
                    },
                    {
                        'price': 4.8,
                        'size': 16.86
                    },
                    {
                        'price': 4.9,
                        'size': 14.2
                    },
                    {
                        'price': 5,
                        'size': 14.09
                    },
                    {
                        'price': 5.2,
                        'size': 19.53
                    },
                    {
                        'price': 5.3,
                        'size': 43.96
                    },
                    {
                        'price': 5.4,
                        'size': 30
                    },
                    {
                        'price': 5.5,
                        'size': 23.74
                    },
                    {
                        'price': 5.6,
                        'size': 7.4
                    },
                    {
                        'price': 5.7,
                        'size': 8.52
                    },
                    {
                        'price': 5.8,
                        'size': 5.7
                    },
                    {
                        'price': 5.9,
                        'size': 38.11
                    },
                    {
                        'price': 6,
                        'size': 109
                    },
                    {
                        'price': 6.2,
                        'size': 267.54
                    },
                    {
                        'price': 6.4,
                        'size': 300.74
                    },
                    {
                        'price': 6.6,
                        'size': 289.09
                    },
                    {
                        'price': 6.8,
                        'size': 26
                    },
                    {
                        'price': 7,
                        'size': 26
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 6.4,
            'removalDate': None,
            'selectionId': 25891932,
            'sp': {
                'actualSP': 6.26,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 65.3
                    },
                    {
                        'price': 4.5,
                        'size': 3.85
                    },
                    {
                        'price': 6.4,
                        'size': 6.26
                    },
                    {
                        'price': 6.6,
                        'size': 4
                    },
                    {
                        'price': 7,
                        'size': 14.65
                    },
                    {
                        'price': 7.2,
                        'size': 6.42
                    },
                    {
                        'price': 7.4,
                        'size': 7.74
                    },
                    {
                        'price': 23,
                        'size': 2.11
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 6.4,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 328.03
                    },
                    {
                        'price': 38,
                        'size': 40
                    },
                    {
                        'price': 6.4,
                        'size': 32.05
                    },
                    {
                        'price': 5.9,
                        'size': 74.04
                    },
                    {
                        'price': 5.6,
                        'size': 69.92
                    },
                    {
                        'price': 5,
                        'size': 23.52
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 6.4
            },
            'status': 'ACTIVE',
            'totalMatched': 568.28
        },
        {
            'adjustmentFactor': 13.07,
            'ex': {
                'availableToBack': [
                    {
                        'price': 2.42,
                        'size': 2
                    },
                    {
                        'price': 2.4,
                        'size': 20.03
                    },
                    {
                        'price': 2.38,
                        'size': 15.67
                    },
                    {
                        'price': 2.34,
                        'size': 96.98
                    },
                    {
                        'price': 2.32,
                        'size': 153.96
                    },
                    {
                        'price': 2.28,
                        'size': 548
                    },
                    {
                        'price': 2.26,
                        'size': 21.75
                    },
                    {
                        'price': 2.24,
                        'size': 31.47
                    },
                    {
                        'price': 2.22,
                        'size': 4.04
                    },
                    {
                        'price': 2.2,
                        'size': 10
                    },
                    {
                        'price': 2.08,
                        'size': 669.69
                    },
                    {
                        'price': 2.06,
                        'size': 182
                    },
                    {
                        'price': 2.02,
                        'size': 300.88
                    },
                    {
                        'price': 2,
                        'size': 197.63
                    },
                    {
                        'price': 1.97,
                        'size': 154.64
                    },
                    {
                        'price': 1.95,
                        'size': 761.33
                    },
                    {
                        'price': 1.94,
                        'size': 50.67
                    },
                    {
                        'price': 1.65,
                        'size': 42.61
                    },
                    {
                        'price': 1.46,
                        'size': 76.53
                    },
                    {
                        'price': 1.4,
                        'size': 100
                    },
                    {
                        'price': 1.35,
                        'size': 98.2
                    },
                    {
                        'price': 1.3,
                        'size': 2
                    },
                    {
                        'price': 1.26,
                        'size': 112.89
                    },
                    {
                        'price': 1.23,
                        'size': 500
                    },
                    {
                        'price': 1.16,
                        'size': 139.81
                    },
                    {
                        'price': 1.13,
                        'size': 2
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.07,
                        'size': 247.8
                    },
                    {
                        'price': 1.06,
                        'size': 170.22
                    },
                    {
                        'price': 1.04,
                        'size': 27.77
                    },
                    {
                        'price': 1.03,
                        'size': 292.44
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 4392.51
                    }
                ],
                'availableToLay': [
                    {
                        'price': 2.46,
                        'size': 174.16
                    },
                    {
                        'price': 2.48,
                        'size': 16.78
                    },
                    {
                        'price': 2.5,
                        'size': 16.68
                    },
                    {
                        'price': 2.52,
                        'size': 16.85
                    },
                    {
                        'price': 2.54,
                        'size': 58.18
                    },
                    {
                        'price': 2.58,
                        'size': 3.64
                    },
                    {
                        'price': 2.6,
                        'size': 3.72
                    },
                    {
                        'price': 2.62,
                        'size': 17.39
                    },
                    {
                        'price': 2.66,
                        'size': 3.49
                    },
                    {
                        'price': 2.68,
                        'size': 47
                    },
                    {
                        'price': 2.8,
                        'size': 17.99
                    },
                    {
                        'price': 2.86,
                        'size': 10.11
                    },
                    {
                        'price': 2.94,
                        'size': 1
                    },
                    {
                        'price': 3.05,
                        'size': 3.94
                    },
                    {
                        'price': 4.2,
                        'size': 7
                    },
                    {
                        'price': 5,
                        'size': 0.75
                    },
                    {
                        'price': 6.4,
                        'size': 60
                    },
                    {
                        'price': 6.8,
                        'size': 3.4
                    },
                    {
                        'price': 27,
                        'size': 10
                    },
                    {
                        'price': 80,
                        'size': 45.53
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 2.34,
                        'size': 239.28
                    },
                    {
                        'price': 2.36,
                        'size': 196.85
                    },
                    {
                        'price': 2.38,
                        'size': 311.58
                    },
                    {
                        'price': 2.4,
                        'size': 78.06
                    },
                    {
                        'price': 2.42,
                        'size': 89.74
                    },
                    {
                        'price': 2.44,
                        'size': 304.56
                    },
                    {
                        'price': 2.46,
                        'size': 226.66
                    },
                    {
                        'price': 2.48,
                        'size': 44.45
                    },
                    {
                        'price': 2.5,
                        'size': 116.35
                    },
                    {
                        'price': 2.52,
                        'size': 97.72
                    },
                    {
                        'price': 2.54,
                        'size': 41.87
                    },
                    {
                        'price': 2.56,
                        'size': 8
                    },
                    {
                        'price': 2.58,
                        'size': 171.71
                    },
                    {
                        'price': 2.6,
                        'size': 176.59
                    },
                    {
                        'price': 2.62,
                        'size': 238.18
                    },
                    {
                        'price': 2.64,
                        'size': 95.47
                    },
                    {
                        'price': 2.66,
                        'size': 55.3
                    },
                    {
                        'price': 2.68,
                        'size': 73.24
                    },
                    {
                        'price': 2.7,
                        'size': 53.43
                    },
                    {
                        'price': 2.72,
                        'size': 75.01
                    },
                    {
                        'price': 2.74,
                        'size': 3.99
                    },
                    {
                        'price': 2.76,
                        'size': 12.52
                    },
                    {
                        'price': 2.78,
                        'size': 6.78
                    },
                    {
                        'price': 2.8,
                        'size': 18.35
                    },
                    {
                        'price': 2.82,
                        'size': 4
                    },
                    {
                        'price': 2.86,
                        'size': 7.14
                    },
                    {
                        'price': 2.9,
                        'size': 17.32
                    },
                    {
                        'price': 2.94,
                        'size': 88
                    },
                    {
                        'price': 3,
                        'size': 89.99
                    },
                    {
                        'price': 3.05,
                        'size': 13.36
                    },
                    {
                        'price': 3.1,
                        'size': 38.14
                    },
                    {
                        'price': 3.2,
                        'size': 27.04
                    },
                    {
                        'price': 3.25,
                        'size': 40.89
                    },
                    {
                        'price': 3.3,
                        'size': 11.64
                    },
                    {
                        'price': 3.4,
                        'size': 8
                    },
                    {
                        'price': 3.45,
                        'size': 76.36
                    },
                    {
                        'price': 3.5,
                        'size': 196.85
                    },
                    {
                        'price': 3.55,
                        'size': 167.17
                    },
                    {
                        'price': 3.6,
                        'size': 169.96
                    },
                    {
                        'price': 3.65,
                        'size': 73.6
                    },
                    {
                        'price': 3.7,
                        'size': 148.11
                    },
                    {
                        'price': 3.75,
                        'size': 63.35
                    },
                    {
                        'price': 3.8,
                        'size': 30.16
                    },
                    {
                        'price': 3.85,
                        'size': 9.62
                    },
                    {
                        'price': 3.9,
                        'size': 9.99
                    },
                    {
                        'price': 4,
                        'size': 30.43
                    },
                    {
                        'price': 4.1,
                        'size': 1.8
                    },
                    {
                        'price': 4.2,
                        'size': 21.12
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 2.46,
            'removalDate': None,
            'selectionId': 21952973,
            'sp': {
                'actualSP': 2.45,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 132.1
                    },
                    {
                        'price': 2.6,
                        'size': 13.84
                    },
                    {
                        'price': 2.62,
                        'size': 2
                    },
                    {
                        'price': 2.74,
                        'size': 7.86
                    },
                    {
                        'price': 2.8,
                        'size': 9.04
                    },
                    {
                        'price': 2.84,
                        'size': 14.27
                    },
                    {
                        'price': 2.94,
                        'size': 9.8
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 2.64,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 198.81
                    },
                    {
                        'price': 5,
                        'size': 27.89
                    },
                    {
                        'price': 2.7,
                        'size': 17.15
                    },
                    {
                        'price': 2.58,
                        'size': 22
                    },
                    {
                        'price': 2.54,
                        'size': 10.01
                    },
                    {
                        'price': 2.44,
                        'size': 63.28
                    },
                    {
                        'price': 2.32,
                        'size': 60.2
                    },
                    {
                        'price': 2.28,
                        'size': 16.62
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 2.46
            },
            'status': 'ACTIVE',
            'totalMatched': 531.22
        },
        {
            'adjustmentFactor': 9.59,
            'ex': {
                'availableToBack': [
                    {
                        'price': 4.6,
                        'size': 11.17
                    },
                    {
                        'price': 4.5,
                        'size': 50.35
                    },
                    {
                        'price': 4.4,
                        'size': 38.17
                    },
                    {
                        'price': 4.3,
                        'size': 9.22
                    },
                    {
                        'price': 4.2,
                        'size': 3.64
                    },
                    {
                        'price': 4.1,
                        'size': 30.83
                    },
                    {
                        'price': 4,
                        'size': 50
                    },
                    {
                        'price': 3.95,
                        'size': 316
                    },
                    {
                        'price': 3.9,
                        'size': 51.72
                    },
                    {
                        'price': 3.75,
                        'size': 17.32
                    },
                    {
                        'price': 3.55,
                        'size': 283.63
                    },
                    {
                        'price': 3.35,
                        'size': 127.66
                    },
                    {
                        'price': 3.25,
                        'size': 24.02
                    },
                    {
                        'price': 3.15,
                        'size': 336.4
                    },
                    {
                        'price': 3.1,
                        'size': 10
                    },
                    {
                        'price': 2.9,
                        'size': 129
                    },
                    {
                        'price': 2.68,
                        'size': 49.46
                    },
                    {
                        'price': 2.52,
                        'size': 149
                    },
                    {
                        'price': 2.12,
                        'size': 125.07
                    },
                    {
                        'price': 2.02,
                        'size': 2
                    },
                    {
                        'price': 1.96,
                        'size': 41.67
                    },
                    {
                        'price': 1.63,
                        'size': 42.61
                    },
                    {
                        'price': 1.41,
                        'size': 67.23
                    },
                    {
                        'price': 1.3,
                        'size': 2
                    },
                    {
                        'price': 1.27,
                        'size': 97.19
                    },
                    {
                        'price': 1.23,
                        'size': 500
                    },
                    {
                        'price': 1.22,
                        'size': 44
                    },
                    {
                        'price': 1.21,
                        'size': 2
                    },
                    {
                        'price': 1.16,
                        'size': 116.63
                    },
                    {
                        'price': 1.13,
                        'size': 2
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.07,
                        'size': 155.51
                    },
                    {
                        'price': 1.06,
                        'size': 19.28
                    },
                    {
                        'price': 1.04,
                        'size': 27.77
                    },
                    {
                        'price': 1.03,
                        'size': 308.14
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 5406.62
                    }
                ],
                'availableToLay': [
                    {
                        'price': 4.7,
                        'size': 18.33
                    },
                    {
                        'price': 4.8,
                        'size': 14.61
                    },
                    {
                        'price': 4.9,
                        'size': 40.17
                    },
                    {
                        'price': 5,
                        'size': 29.94
                    },
                    {
                        'price': 5.1,
                        'size': 25.17
                    },
                    {
                        'price': 5.2,
                        'size': 14.45
                    },
                    {
                        'price': 5.3,
                        'size': 0.75
                    },
                    {
                        'price': 5.4,
                        'size': 11.54
                    },
                    {
                        'price': 5.6,
                        'size': 11.11
                    },
                    {
                        'price': 5.7,
                        'size': 3.64
                    },
                    {
                        'price': 5.8,
                        'size': 9.37
                    },
                    {
                        'price': 5.9,
                        'size': 21
                    },
                    {
                        'price': 6.2,
                        'size': 2
                    },
                    {
                        'price': 9,
                        'size': 1.66
                    },
                    {
                        'price': 9.2,
                        'size': 41
                    },
                    {
                        'price': 10.5,
                        'size': 12.62
                    },
                    {
                        'price': 42,
                        'size': 10
                    },
                    {
                        'price': 55,
                        'size': 0.5
                    },
                    {
                        'price': 95,
                        'size': 45.53
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 4.2,
                        'size': 32
                    },
                    {
                        'price': 4.3,
                        'size': 12
                    },
                    {
                        'price': 4.5,
                        'size': 9.08
                    },
                    {
                        'price': 4.7,
                        'size': 29.46
                    },
                    {
                        'price': 4.8,
                        'size': 60.94
                    },
                    {
                        'price': 4.9,
                        'size': 273.36
                    },
                    {
                        'price': 5,
                        'size': 278.04
                    },
                    {
                        'price': 5.1,
                        'size': 408.15
                    },
                    {
                        'price': 5.2,
                        'size': 348.03
                    },
                    {
                        'price': 5.3,
                        'size': 98.11
                    },
                    {
                        'price': 5.4,
                        'size': 11.35
                    },
                    {
                        'price': 5.5,
                        'size': 52.98
                    },
                    {
                        'price': 5.7,
                        'size': 4
                    },
                    {
                        'price': 5.8,
                        'size': 10.12
                    },
                    {
                        'price': 5.9,
                        'size': 7.99
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 4.7,
            'removalDate': None,
            'selectionId': 19381604,
            'sp': {
                'actualSP': 4.6,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 67.12
                    },
                    {
                        'price': 1.11,
                        'size': 5
                    },
                    {
                        'price': 4.7,
                        'size': 2.76
                    },
                    {
                        'price': 5.1,
                        'size': 5.43
                    },
                    {
                        'price': 5.3,
                        'size': 2
                    },
                    {
                        'price': 5.5,
                        'size': 5.17
                    },
                    {
                        'price': 5.8,
                        'size': 6.59
                    },
                    {
                        'price': 5.9,
                        'size': 11.93
                    },
                    {
                        'price': 6,
                        'size': 15.35
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 4.7,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 116.34
                    },
                    {
                        'price': 25,
                        'size': 20
                    },
                    {
                        'price': 5,
                        'size': 47.27
                    },
                    {
                        'price': 4.9,
                        'size': 10.03
                    },
                    {
                        'price': 4.8,
                        'size': 16.62
                    },
                    {
                        'price': 4.7,
                        'size': 73.6
                    },
                    {
                        'price': 4.6,
                        'size': 19.71
                    },
                    {
                        'price': 4.4,
                        'size': 69.66
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 4.86
            },
            'status': 'ACTIVE',
            'totalMatched': 29.46
        },
        {
            'adjustmentFactor': 16.16,
            'ex': {
                'availableToBack': [
                    {
                        'price': 3,
                        'size': 24.89
                    },
                    {
                        'price': 2.98,
                        'size': 4.42
                    },
                    {
                        'price': 2.96,
                        'size': 55.61
                    },
                    {
                        'price': 2.94,
                        'size': 106.37
                    },
                    {
                        'price': 2.92,
                        'size': 41.57
                    },
                    {
                        'price': 2.9,
                        'size': 65.94
                    },
                    {
                        'price': 2.88,
                        'size': 474.36
                    },
                    {
                        'price': 2.86,
                        'size': 40.8
                    },
                    {
                        'price': 2.76,
                        'size': 9.53
                    },
                    {
                        'price': 2.74,
                        'size': 26.59
                    },
                    {
                        'price': 2.42,
                        'size': 105.63
                    },
                    {
                        'price': 2.38,
                        'size': 524.1
                    },
                    {
                        'price': 2.34,
                        'size': 111.94
                    },
                    {
                        'price': 2.32,
                        'size': 4.42
                    },
                    {
                        'price': 2.28,
                        'size': 244.38
                    },
                    {
                        'price': 2.24,
                        'size': 243.82
                    },
                    {
                        'price': 2.2,
                        'size': 602.72
                    },
                    {
                        'price': 2.14,
                        'size': 30.97
                    },
                    {
                        'price': 2,
                        'size': 188
                    },
                    {
                        'price': 1.88,
                        'size': 35
                    },
                    {
                        'price': 1.64,
                        'size': 42.61
                    },
                    {
                        'price': 1.6,
                        'size': 5
                    },
                    {
                        'price': 1.59,
                        'size': 67.8
                    },
                    {
                        'price': 1.57,
                        'size': 84.44
                    },
                    {
                        'price': 1.43,
                        'size': 70.28
                    },
                    {
                        'price': 1.41,
                        'size': 5.18
                    },
                    {
                        'price': 1.35,
                        'size': 35
                    },
                    {
                        'price': 1.3,
                        'size': 2
                    },
                    {
                        'price': 1.26,
                        'size': 113.64
                    },
                    {
                        'price': 1.25,
                        'size': 212.11
                    },
                    {
                        'price': 1.23,
                        'size': 500
                    },
                    {
                        'price': 1.15,
                        'size': 88
                    },
                    {
                        'price': 1.13,
                        'size': 149.28
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.08,
                        'size': 77
                    },
                    {
                        'price': 1.06,
                        'size': 214.42
                    },
                    {
                        'price': 1.04,
                        'size': 27.77
                    },
                    {
                        'price': 1.03,
                        'size': 273.75
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 6610.31
                    }
                ],
                'availableToLay': [
                    {
                        'price': 3.1,
                        'size': 12.02
                    },
                    {
                        'price': 3.15,
                        'size': 19.51
                    },
                    {
                        'price': 3.2,
                        'size': 23.69
                    },
                    {
                        'price': 3.25,
                        'size': 3.03
                    },
                    {
                        'price': 3.3,
                        'size': 22.75
                    },
                    {
                        'price': 3.35,
                        'size': 37.56
                    },
                    {
                        'price': 3.4,
                        'size': 3.52
                    },
                    {
                        'price': 3.7,
                        'size': 34
                    },
                    {
                        'price': 4.2,
                        'size': 25.26
                    },
                    {
                        'price': 4.9,
                        'size': 2
                    },
                    {
                        'price': 6.2,
                        'size': 60
                    },
                    {
                        'price': 7.6,
                        'size': 3.28
                    },
                    {
                        'price': 24,
                        'size': 10
                    },
                    {
                        'price': 80,
                        'size': 45.53
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 2.98,
                        'size': 162.68
                    },
                    {
                        'price': 3,
                        'size': 463.99
                    },
                    {
                        'price': 3.05,
                        'size': 261.44
                    },
                    {
                        'price': 3.1,
                        'size': 280.36
                    },
                    {
                        'price': 3.15,
                        'size': 278.76
                    },
                    {
                        'price': 3.2,
                        'size': 199.85
                    },
                    {
                        'price': 3.25,
                        'size': 205.76
                    },
                    {
                        'price': 3.3,
                        'size': 142.97
                    },
                    {
                        'price': 3.35,
                        'size': 303.7
                    },
                    {
                        'price': 3.4,
                        'size': 226.9
                    },
                    {
                        'price': 3.45,
                        'size': 367.6
                    },
                    {
                        'price': 3.5,
                        'size': 331.88
                    },
                    {
                        'price': 3.55,
                        'size': 989.77
                    },
                    {
                        'price': 3.6,
                        'size': 106.5
                    },
                    {
                        'price': 3.65,
                        'size': 45.66
                    },
                    {
                        'price': 3.7,
                        'size': 0.21
                    },
                    {
                        'price': 3.75,
                        'size': 19.1
                    },
                    {
                        'price': 3.8,
                        'size': 4.06
                    },
                    {
                        'price': 3.85,
                        'size': 8
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 3.0,
            'removalDate': None,
            'selectionId': 27388539,
            'sp': {
                'actualSP': 3.03,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 101.27
                    },
                    {
                        'price': 1.11,
                        'size': 5
                    },
                    {
                        'price': 3.05,
                        'size': 10.89
                    },
                    {
                        'price': 3.15,
                        'size': 2
                    },
                    {
                        'price': 3.25,
                        'size': 7.86
                    },
                    {
                        'price': 3.3,
                        'size': 9.04
                    },
                    {
                        'price': 3.45,
                        'size': 14.27
                    },
                    {
                        'price': 3.5,
                        'size': 8.76
                    },
                    {
                        'price': 3.55,
                        'size': 4.77
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 2.82,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 102.97
                    },
                    {
                        'price': 5,
                        'size': 24.04
                    },
                    {
                        'price': 3.1,
                        'size': 17.15
                    },
                    {
                        'price': 3,
                        'size': 32
                    },
                    {
                        'price': 2.82,
                        'size': 63.39
                    },
                    {
                        'price': 2.74,
                        'size': 60.28
                    },
                    {
                        'price': 2.64,
                        'size': 16.62
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 3.01
            },
            'status': 'ACTIVE',
            'totalMatched': 725.43
        },
        {
            'adjustmentFactor': 3.38,
            'ex': {
                'availableToBack': [
                    {
                        'price': 14,
                        'size': 22.34
                    },
                    {
                        'price': 13.5,
                        'size': 14.06
                    },
                    {
                        'price': 13,
                        'size': 20.23
                    },
                    {
                        'price': 12.5,
                        'size': 7.16
                    },
                    {
                        'price': 12,
                        'size': 22.72
                    },
                    {
                        'price': 11.5,
                        'size': 113.81
                    },
                    {
                        'price': 10,
                        'size': 3.01
                    },
                    {
                        'price': 9.6,
                        'size': 4.25
                    },
                    {
                        'price': 9.4,
                        'size': 2
                    },
                    {
                        'price': 9.2,
                        'size': 102.61
                    },
                    {
                        'price': 8.8,
                        'size': 11.13
                    },
                    {
                        'price': 7.6,
                        'size': 0.93
                    },
                    {
                        'price': 7.4,
                        'size': 113
                    },
                    {
                        'price': 7,
                        'size': 56
                    },
                    {
                        'price': 6.2,
                        'size': 3.06
                    },
                    {
                        'price': 6,
                        'size': 30
                    },
                    {
                        'price': 5.8,
                        'size': 106.17
                    },
                    {
                        'price': 3.1,
                        'size': 2
                    },
                    {
                        'price': 2.5,
                        'size': 26.67
                    },
                    {
                        'price': 2.36,
                        'size': 33.64
                    },
                    {
                        'price': 2.02,
                        'size': 2
                    },
                    {
                        'price': 2,
                        'size': 105
                    },
                    {
                        'price': 1.63,
                        'size': 92.71
                    },
                    {
                        'price': 1.41,
                        'size': 5.18
                    },
                    {
                        'price': 1.3,
                        'size': 2
                    },
                    {
                        'price': 1.23,
                        'size': 500
                    },
                    {
                        'price': 1.13,
                        'size': 2
                    },
                    {
                        'price': 1.12,
                        'size': 44.93
                    },
                    {
                        'price': 1.06,
                        'size': 219.28
                    },
                    {
                        'price': 1.04,
                        'size': 27.77
                    },
                    {
                        'price': 1.03,
                        'size': 2.35
                    },
                    {
                        'price': 1.02,
                        'size': 6792
                    },
                    {
                        'price': 1.01,
                        'size': 22066.39
                    }
                ],
                'availableToLay': [
                    {
                        'price': 17,
                        'size': 4.04
                    },
                    {
                        'price': 17.5,
                        'size': 9.31
                    },
                    {
                        'price': 18,
                        'size': 9.3
                    },
                    {
                        'price': 19,
                        'size': 5.73
                    },
                    {
                        'price': 19.5,
                        'size': 8.02
                    },
                    {
                        'price': 20,
                        'size': 5.26
                    },
                    {
                        'price': 21,
                        'size': 5
                    },
                    {
                        'price': 22,
                        'size': 2.27
                    },
                    {
                        'price': 23,
                        'size': 9.31
                    },
                    {
                        'price': 24,
                        'size': 0.76
                    },
                    {
                        'price': 26,
                        'size': 7.76
                    },
                    {
                        'price': 36,
                        'size': 3.68
                    },
                    {
                        'price': 65,
                        'size': 7.26
                    },
                    {
                        'price': 180,
                        'size': 0.1
                    },
                    {
                        'price': 320,
                        'size': 0.1
                    },
                    {
                        'price': 930,
                        'size': 1.04
                    },
                    {
                        'price': 1000,
                        'size': 2
                    }
                ],
                'tradedVolume': [
                    {
                        'price': 6,
                        'size': 18.11
                    },
                    {
                        'price': 6.2,
                        'size': 3.97
                    },
                    {
                        'price': 6.4,
                        'size': 16
                    },
                    {
                        'price': 6.6,
                        'size': 10.41
                    },
                    {
                        'price': 6.8,
                        'size': 11.37
                    },
                    {
                        'price': 7,
                        'size': 19.02
                    },
                    {
                        'price': 7.2,
                        'size': 12.76
                    },
                    {
                        'price': 8,
                        'size': 4
                    },
                    {
                        'price': 9.4,
                        'size': 2
                    },
                    {
                        'price': 11,
                        'size': 33.99
                    },
                    {
                        'price': 11.5,
                        'size': 33.34
                    },
                    {
                        'price': 12,
                        'size': 35.26
                    },
                    {
                        'price': 12.5,
                        'size': 19.21
                    },
                    {
                        'price': 13,
                        'size': 64.62
                    },
                    {
                        'price': 13.5,
                        'size': 48.37
                    },
                    {
                        'price': 14,
                        'size': 39.98
                    },
                    {
                        'price': 14.5,
                        'size': 21.9
                    },
                    {
                        'price': 15,
                        'size': 16.48
                    },
                    {
                        'price': 15.5,
                        'size': 18.11
                    },
                    {
                        'price': 16,
                        'size': 9.26
                    },
                    {
                        'price': 16.5,
                        'size': 10.18
                    },
                    {
                        'price': 17,
                        'size': 61.41
                    },
                    {
                        'price': 17.5,
                        'size': 17.13
                    },
                    {
                        'price': 18,
                        'size': 20
                    },
                    {
                        'price': 18.5,
                        'size': 6.57
                    },
                    {
                        'price': 19,
                        'size': 18.86
                    },
                    {
                        'price': 19.5,
                        'size': 8.96
                    }
                ]
            },
            'handicap': 0,
            'lastPriceTraded': 14.0,
            'removalDate': None,
            'selectionId': 25797865,
            'sp': {
                'actualSP': 14.7,
                'backStakeTaken': [
                    {
                        'price': 1.01,
                        'size': 96.37
                    },
                    {
                        'price': 1.7,
                        'size': 2
                    },
                    {
                        'price': 10,
                        'size': 2
                    },
                    {
                        'price': 13.5,
                        'size': 3.7
                    },
                    {
                        'price': 21,
                        'size': 10.47
                    },
                    {
                        'price': 22,
                        'size': 5.47
                    },
                    {
                        'price': 25,
                        'size': 3.95
                    },
                    {
                        'price': 470,
                        'size': 1.78
                    }
                ],
                'farPrice': 10.05,
                'layLiabilityTaken': [
                    {
                        'price': 1000,
                        'size': 709.44
                    },
                    {
                        'price': 17,
                        'size': 22
                    },
                    {
                        'price': 16,
                        'size': 10.06
                    },
                    {
                        'price': 15.5,
                        'size': 77.67
                    },
                    {
                        'price': 14,
                        'size': 90.06
                    },
                    {
                        'price': 5,
                        'size': 24.4
                    },
                    {
                        'price': 1.04,
                        'size': 35.71
                    }
                ],
                'nearPrice': 15.53
            },
            'status': 'ACTIVE',
            'totalMatched': 96.47
        }
    ],
    'runnersVoidable': False,
    'status': 'SUSPENDED',
    'streaming_snap': True,
    'streaming_unique_id': 0,
    'streaming_update': {
        'con': True,
        'id': '1.172557162',
        'img': False,
        'marketDefinition': {
            'betDelay': 1,
            'bettingType': 'ODDS',
            'bspMarket': True,
            'bspReconciled': True,
            'complete': True,
            'countryCode': 'GB',
            'crossMatching': False,
            'discountAllowed': True,
            'eventId': '29987033',
            'eventName': 'Sand  31st Aug',
            'eventTypeId': '7',
            'inPlay': True,
            'marketBaseRate': 5.0,
            'marketTime': '2020-08-31T18:30:00.000Z',
            'marketType': 'PLACE',
            'name': 'To Be Placed',
            'numberOfActiveRunners': 9,
            'numberOfWinners': 3,
            'openDate': '2020-08-31T14:00:00.000Z',
            'persistenceEnabled': True,
            'regulators': [
                'MR_INT'
            ],
            'runners': [
                {
                    'adjustmentFactor': 27.12,
                    'bsp': 2.14,
                    'id': 26374770,
                    'name': 'Arij',
                    'sortPriority': 1,
                    'status': 'ACTIVE'
                },
                {
                    'adjustmentFactor': 24.68,
                    'bsp': 2.17,
                    'id': 28007114,
                    'name': 'Kitzbuhel',
                    'sortPriority': 2,
                    'status': 'ACTIVE'
                },
                {
                    'adjustmentFactor': 24.02,
                    'bsp': 2.62,
                    'id': 430775,
                    'name': 'Mephisto',
                    'sortPriority': 3,
                    'status': 'ACTIVE'
                },
                {
                    'adjustmentFactor': 22.19,
                    'bsp': 1.87,
                    'id': 22864389,
                    'name': 'Sir Canford',
                    'sortPriority': 4,
                    'status': 'ACTIVE'
                },
                {
                    'adjustmentFactor': 16.16,
                    'bsp': 3.03,
                    'id': 27388539,
                    'name': 'En Famille',
                    'sortPriority': 5,
                    'status': 'ACTIVE'
                },
                {
                    'adjustmentFactor': 15.63,
                    'bsp': 6.26,
                    'id': 25891932,
                    'name': 'Noble Dawn',
                    'sortPriority': 6,
                    'status': 'ACTIVE'
                },
                {
                    'adjustmentFactor': 13.07,
                    'bsp': 2.45,
                    'id': 21952973,
                    'name': 'Twpsyn',
                    'sortPriority': 7,
                    'status': 'ACTIVE'
                },
                {
                    'adjustmentFactor': 9.59,
                    'bsp': 4.6,
                    'id': 19381604,
                    'name': 'Isle Of Wolves',
                    'sortPriority': 8,
                    'status': 'ACTIVE'
                },
                {
                    'adjustmentFactor': 3.38,
                    'bsp': 14.7,
                    'id': 25797865,
                    'name': 'Nibras Wish',
                    'sortPriority': 9,
                    'status': 'ACTIVE'
                }
            ],
            'runnersVoidable': False,
            'status': 'SUSPENDED',
            'suspendTime': '2020-08-31T18:30:00.000Z',
            'timezone': 'Europe/London',
            'turnInPlayEnabled': True,
            'venue': 'Sandown',
            'version': 3342028375
        },
        'rc': []
    },
    'totalAvailable': None,
    'totalMatched': 46114.73,
    'version': 3342028375
}

EXAMPLE_RUNNER_BOOK = EXAMPLE_MARKET_BOOK['runners'][0]

CSS_STYLE = """
<style>
#betfairviz * {
  all: revert;
}
#betfairviz html {
  color: #000;
  background: #fff;
}
#betfairviz body,
#betfairviz div,
#betfairviz h3,
#betfairviz td,
#betfairviz th {
  margin: 0;
  padding: 0;
  line-height: 1;
}
#betfairviz table {
  border-collapse: collapse;
  border-spacing: 0;
}
#betfairviz th {
  font-style: normal;
  font-weight: 400;
}
#betfairviz th {
  text-align: left;
}
#betfairviz h3 {
  font-size: 100%;
  font-weight: 400;
}
#betfairviz button {
  border-radius: 0;
}
#betfairviz .bf-row {
  line-height: 0;
}
#betfairviz body,
#betfairviz html {
  height: 100%;
}
#betfairviz html {
  font-size: 62.5%;
}
#betfairviz body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 11px;
}
#betfairviz .marketview-list-runners-component {
  margin-bottom: 0;
  position: relative;
}
#betfairviz .marketview-list-runners-component .mv-runner-list-container {
  padding: 0 8px;
}
#betfairviz .marketview-list-runners-component .runner-list-wrapper {
  overflow-x: auto;
  overflow-y: hidden;
}
#betfairviz .marketview-list-runners-component .market-graph-container {
  float: left;
  overflow: hidden;
  width: 13px;
  height: 29px;
  padding-left: 2px;
}
#betfairviz .marketview-list-runners-component .mv-runner-list {
  min-height: 1px;
  height: 100%;
  width: 100%;
  border: 0;
  border-spacing: 0;
  padding: 0;
}
#betfairviz .marketview-list-runners-component .bet-buttons .back,
#betfairviz .marketview-list-runners-component .bet-buttons .lay {
  background-color: #fff;
}
#betfairviz .marketview-list-runners-component .bet-buttons .back-selection-button {
  background-color: #a6d8ff;
}
#betfairviz .marketview-list-runners-component .bet-buttons .lay-selection-button {
  background-color: #fac9d4;
}
#betfairviz .marketview-list-runners-component .runner-line {
  height: 100%;
  border-bottom: 1px solid #dfdfdf;
}
#betfairviz .marketview-list-runners-component .runner-line .back,
#betfairviz .marketview-list-runners-component .runner-line .lay {
  border: 0;
  margin: 0;
  padding: 0;
}
#betfairviz .marketview-list-runners-component .runner-line .back,
#betfairviz .marketview-list-runners-component .runner-line .lay {
  width: 100%;
  height: 100%;
}
#betfairviz .marketview-list-runners-component .runner-line .back {
  border-left: 1px solid #dfdfdf;
}
#betfairviz .marketview-list-runners-component .runner-line .back.back-selection-button {
  border-right: 1px solid #fff;
  border-left: 0;
}
#betfairviz .marketview-list-runners-component .runner-line .lay {
  border-right: 1px solid #dfdfdf;
}
#betfairviz .marketview-list-runners-component .runner-line .lay.lay-selection-button {
  border-right: 0;
}
#betfairviz .marketview-list-runners-component .runner-line .price {
  font-weight: 700;
  display: block;
}
#betfairviz .marketview-list-runners-component .runner-line .size {
  display: block;
}
#betfairviz .marketview-list-runners-component .runner-line .bet-buttons {
  width: 8%;
  text-align: center;
  overflow: hidden;
}
#betfairviz .marketview-list-runners-component .runner-line .back-cell,
#betfairviz .marketview-list-runners-component .runner-line .lay-cell {
  line-height: 0;
  height: 100%;
}
#betfairviz .marketview-list-runners-component .runner-line .back-cell.first-lay-cell,
#betfairviz .marketview-list-runners-component .runner-line .back-cell.last-back-cell,
#betfairviz .marketview-list-runners-component .runner-line .lay-cell.first-lay-cell,
#betfairviz .marketview-list-runners-component .runner-line .lay-cell.last-back-cell {
  border-bottom: 1px solid #fff;
}
#betfairviz .marketview-list-runners-component .runner-line:first-child .back-cell,
#betfairviz .marketview-list-runners-component .runner-line:first-child .lay-cell,
#betfairviz .marketview-list-runners-component .runner-line:first-child .new-runner-info {
  border-top: 1px solid #dfdfdf;
}
#betfairviz .marketview-list-runners-component .runner-line:last-child .back-cell.last-back-cell,
#betfairviz .marketview-list-runners-component .runner-line:last-child .lay-cell.first-lay-cell {
  overflow: hidden;
  border-bottom: 1px solid #dfdfdf;
}
#betfairviz .marketview-list-runners-component .runner-line:last-child .back,
#betfairviz .marketview-list-runners-component .runner-line:last-child .lay {
  margin-bottom: 2px;
}
#betfairviz .marketview-list-runners-component .bet-buttons .back:hover,
#betfairviz .marketview-list-runners-component .bet-buttons .lay:hover {
  background-color: #dfdfdf;
}
#betfairviz .marketview-list-runners-component .bet-buttons .back-selection-button:hover {
  background-color: #75c2fd;
}
#betfairviz .marketview-list-runners-component .bet-buttons .lay-selection-button:hover {
  background-color: #f694aa;
}
#betfairviz .marketview-list-runners-component .mv-runner-list.fixed-size .bet-buttons {
  min-width: 60px;
}
#betfairviz .marketview-list-runners-component .runner-item {
  margin: 0;
  border-bottom: 1px solid #dfdfdf;
}
#betfairviz .marketview-list-runners-component .runner-item:first-child,
#betfairviz .marketview-list-runners-component .runner-line:first-child {
  margin-top: 1px;
  border-top: 1px solid #dfdfdf;
}
#betfairviz .marketview-list-runners-component .runner-item.middle .runner-data-container {
  line-height: 26px;
}
#betfairviz .marketview-list-runners-component .runner-item .runner-data-container .runner-info .name {
  float: none;
}
#betfairviz .marketview-list-runners-component .runner-inner-container-header-overlay,
#betfairviz .marketview-list-runners-component .runner-list-overlay {
  background: #fff;
}
@media screen and (max-width: 80em) {
  #betfairviz .marketview-list-runners-component .mv-bet-button .bet-button-size,
  #betfairviz .marketview-list-runners-component .size {
    font-size: 10px;
  }
}
@media screen and (min-width: 80em) {
  #betfairviz .marketview-list-runners-component .mv-bet-button .bet-button-size,
  #betfairviz .marketview-list-runners-component .size {
    font-size: 11px;
  }
}
#betfairviz .marketview-container .loading-wrapper {
  margin-top: 70px;
}
@media only screen and (max-width: 1024px) {
  #betfairviz .market-going-inplay {
    max-width: 90px;
  }
}
@media only screen and (max-width: 1024px), only screen and (max-width: 1279px) {
  #betfairviz .bf-market-view-scroll .market-info-container {
    width: 100%;
    float: left;
    padding-bottom: 5px;
  }
}
#betfairviz .marketview-list-runners-component .runner-line.loser-runner .runner-data-container,
#betfairviz .marketview-list-runners-component .runner-line.winner-runner .runner-data-container {
  float: none;
}
#betfairviz .marketview-list-runners-component.market-closed .loser-runner .runner-info-container .runner-data-container,
#betfairviz .marketview-list-runners-component.market-closed .loser-runner .runner-info-left-elems-container {
  -moz-opacity: 0.13;
  -khtml-opacity: 0.13;
  -webkit-opacity: 0.13;
  opacity: 0.13;
}
#betfairviz .marketview-list-runners-component .mv-runner-list .runner-line:last-child .back,
#betfairviz .marketview-list-runners-component .mv-runner-list .runner-line:last-child .lay {
  margin-bottom: 0;
}
#betfairviz .runners-header {
  margin: 5px 8px 0;
  width: calc(100% - 16px);
  font-family: Arial, Helvetica, sans-serif;
  font-size: 11px;
}
#betfairviz .rh-line {
  vertical-align: bottom;
}
#betfairviz .rh-runner-name-header {
  line-height: 18px;
}
#betfairviz .rh-selections-count-label {
  padding-right: 15%;
}
#betfairviz .rh-book-percentage {
  width: 8%;
}
#betfairviz .rh-select-all-buttons {
  width: 16%;
}
#betfairviz .rh-lay-book-percentage,
#betfairviz .rh-select-back-all-button {
  text-align: right;
}
#betfairviz .rh-back-all,
#betfairviz .rh-lay-all {
  width: 65px;
  padding: 3px 5px;
  height: 18px;
  line-height: 13px;
  font-size: 11px;
  font-weight: 700;
  border: 0;
  cursor: pointer;
}
#betfairviz .rh-back-all-label,
#betfairviz .rh-lay-all-label {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  display: block;
}
#betfairviz .rh-back-all {
  float: right;
  margin-right: 1px;
  background-color: #a6d8ff;
}
#betfairviz .rh-back-all:hover {
  background-color: #75c2fd;
}
#betfairviz .rh-back-all:focus {
  outline: 0;
}
#betfairviz .rh-lay-all {
  float: left;
  background-color: #fac9d4;
}
#betfairviz .rh-lay-all:hover {
  background-color: #f694aa;
}
#betfairviz .rh-lay-all:focus {
  outline: 0;
}
#betfairviz .rh-label-all {
  width: 16%;
  color: #7f7f7f;
  text-align: center;
}
#betfairviz .rh-label-back,
#betfairviz .rh-label-lay {
  color: #7f7f7f;
  width: calc(50% - 10px);
  padding: 3px 5px;
  text-align: center;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
#betfairviz .rh-label-back {
  float: right;
  margin-right: 1px;
}
#betfairviz .rh-label-lay {
  float: left;
}
#betfairviz .rh-label-all.is-small {
  width: 8%;
}
#betfairviz .rh-label-all.is-small .rh-label-back,
#betfairviz .rh-label-all.is-small .rh-label-lay {
  width: calc(100% - 10px);
  min-width: 50px;
}
#betfairviz .bf-header-visibility {
  display: block;
  height: 76px;
  background-color: #dfe5e5;
  padding-left: 9999px;
}
@media only screen and (max-width: 896px) {
  #betfairviz .bf-header-visibility {
    height: 103px;
  }
}
#betfairviz .sports-header-container .sports {
  background: #303030;
  padding: 5px 8px 4px;
  min-height: 50px;
  position: relative;
}
#betfairviz .sports-header-container .sports .date {
  color: #fff;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
#betfairviz .sports-header-container .sports .title {
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  font-size: 20px;
  line-height: 24px;
}
#betfairviz .sports-header-container .sports .title {
  padding-left: 22px;
}
#betfairviz .sports-header-container .sports .date {
  font-size: 12px;
  line-height: 18px;
  margin-top: 4px;
}
#betfairviz html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
#betfairviz body {
  margin: 0;
}
#betfairviz header,
#betfairviz summary {
  display: block;
}
#betfairviz [hidden],
#betfairviz template {
  display: none;
}
#betfairviz a {
  background: 0 0;
}
#betfairviz a:active,
#betfairviz a:hover {
  outline: 0;
}
#betfairviz b {
  font-weight: 700;
}
#betfairviz mark {
  background: #ff0;
  color: #000;
}
#betfairviz small {
  font-size: 80%;
}
#betfairviz button {
  color: inherit;
  font: inherit;
  margin: 0;
}
#betfairviz button {
  overflow: visible;
}
#betfairviz button {
  text-transform: none;
}
#betfairviz button {
  -webkit-appearance: button;
  cursor: pointer;
}
#betfairviz button[disabled] {
  cursor: default;
}
#betfairviz button::-moz-focus-inner {
  border: 0;
  padding: 0;
}
#betfairviz table {
  border-collapse: collapse;
  border-spacing: 0;
}
#betfairviz td,
#betfairviz th {
  padding: 0;
}
#betfairviz .bf-row {
  letter-spacing: -0.31em;
  text-rendering: optimizespeed;
  display: -webkit-flex;
  display: -ms-flexbox;
  -ms-flex-flow: row wrap;
  margin-bottom: 10px;
  margin-left: -5px;
  margin-right: -5px;
}
#betfairviz [class*="bf-col-"] {
  box-sizing: border-box;
  padding-left: 5px;
  padding-right: 5px;
  display: inline-block;
  zoom: 1;
  letter-spacing: normal;
  word-spacing: normal;
  vertical-align: top;
  text-rendering: auto;
}
#betfairviz .bf-col-9-24 {
  width: 37.5%;
}
#betfairviz .bf-col-15-24 {
  width: 62.5%;
}
#betfairviz .bf-col-24-24 {
  width: 100%;
}
#betfairviz .mv-bet-button,
#betfairviz .mv-header-container {
  font-family: Tahoma, Verdana, Arial, sans-serif;
  font-size: 11px;
}
#betfairviz .mv-header-container .market-status .market-status-label {
  margin-left: 5px;
}
#betfairviz .mv-bet-button {
  width: 100%;
  height: 100%;
  border-width: 0;
  background-color: #fff;
  outline: 0;
  cursor: pointer;
}
#betfairviz .mv-bet-button.changed {
  -webkit-animation-name: highlightDefault;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: highlightDefault;
  -moz-animation-duration: 0.3s;
  animation-name: highlightDefault;
  animation-duration: 0.3s;
}
#betfairviz .mv-bet-button:hover {
  background-color: #dfdfdf;
}
#betfairviz .mv-bet-button .bet-button-price,
#betfairviz .mv-bet-button .bet-button-size {
  text-align: center;
  display: block;
}
#betfairviz .mv-bet-button .bet-button-price {
  font-weight: 700;
}
#betfairviz .mv-bet-button.back-selection-button {
  background-color: #a6d8ff;
}
#betfairviz .mv-bet-button.back-selection-button:hover {
  background-color: #75c2fd;
}
#betfairviz .mv-bet-button.lay-selection-button {
  background-color: #fac9d1;
}
#betfairviz .mv-bet-button.lay-selection-button:hover {
  background-color: #f694aa;
}
#betfairviz .runner-info {
  font-size: 11px;
  padding-right: 5px;
}
#betfairviz .runner-info .name {
  float: left;
}
#betfairviz .runner-info .runner-name {
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  overflow: hidden;
  margin: 0;
  white-space: nowrap;
}
#betfairviz .runner-info .runner-name {
  font-weight: 700;
  line-height: 26px;
  padding: 2px 5px 1px;
}
#betfairviz .market-graph {
  border: 0;
}
@keyframes highlightBack {
  0% {
    background-color: #a6d8ff;
  }
  50% {
    background-color: #ff0;
  }
  100% {
    background-color: #a6d8ff;
  }
}
@keyframes highlightLay {
  0% {
    background-color: #fac9d1;
  }
  50% {
    background-color: #ff0;
  }
  100% {
    background-color: #fac9d1;
  }
}
@keyframes highlightDefault {
  0% {
    background-color: #fff;
  }
  50% {
    background-color: #ff0;
  }
  100% {
    background-color: #fff;
  }
}
#betfairviz .bf-bet-button {
  font-family: Tahoma, Verdana, Arial, sans-serif;
  font-size: 11px;
  width: 100%;
  height: 100%;
  border-width: 0;
  background-color: #fff;
  outline: 0;
  cursor: pointer;
}
#betfairviz .bf-bet-button:hover {
  background-color: #dfdfdf;
}
#betfairviz .bf-bet-button .bet-button-price,
#betfairviz .bf-bet-button .bet-button-size {
  text-align: center;
  display: block;
}
#betfairviz .bf-bet-button .bet-button-price {
  font-weight: 700;
}
#betfairviz .bf-bet-button.back-selection-button {
  background-color: #a6d8ff;
}
#betfairviz .bf-bet-button.back-selection-button:hover {
  background-color: #75c2fd;
}
#betfairviz .bf-bet-button.lay-selection-button {
  background-color: #fac9d1;
}
#betfairviz .bf-bet-button.lay-selection-button:hover {
  background-color: #f694aa;
}
#betfairviz .ladder-table {
  display: block;
  border-collapse: collapse;
  overflow-y: auto;
  overflow-x: hidden;
  max-height: 644px;
  border: 1px solid #F0F1F5;
  font: normal normal normal 12px "Arial", "sans-serif";
}
#betfairviz .ladder-table thead {
  display: table;
  width: 100%;
}
#betfairviz .ladder-table th {
  height: 18px;
  padding: 5px;
  text-align: center;
  font: normal normal bold 12px "Arial", "sans-serif";
}
#betfairviz .ladder-table .titles th {
  background-color: #F0F1F5;
}
#betfairviz .ladder-table tbody tr {
  display: table;
  width: 100%;
  table-layout: fixed;
}
#betfairviz .ladder-table td {
  padding: 5px;
  font: normal normal normal 12px "Arial", "sans-serif";
  border: 1px solid #DFDFDf;
  border-bottom: 0;
  height: 14px;
}
#betfairviz .ladder-table .item td .price {
  text-align: left;
}
#betfairviz .ladder-table .item td.price.back-color,
#betfairviz .ladder-table .item td.back.back-color {
  background-color: #A6D8FF;
}
#betfairviz .ladder-table .item td.price.lay-color,
#betfairviz .ladder-table .item td.lay.lay-color {
  background-color: #FAC9D1;
}
#betfairviz .ladder-table .item td.back,
#betfairviz .ladder-table .item td.lay,
#betfairviz .ladder-table .item td.traded {
  text-align: right;
}
#betfairviz .mv-header-container .total-matched,
#betfairviz .mv-header-container .total-matched-label {
  font-family: Tahoma, Verdana, Arial, sans-serif;
  font-size: 11px;
  color: #273a47;
  white-space: nowrap;
}
#betfairviz .mv-header-container .total-matched-label {
  padding: 3px;
}
#betfairviz .mv-header-container .total-matched {
  font-weight: 700;
  margin-right: 5px;
}
#betfairviz .mv-header-container .mv-header-total-matched-wrapper {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-flow: row nowrap;
  flex-flow: row nowrap;
  -ms-flex-align: center;
  align-items: center;
}
#betfairviz .mv-header-container
  .mv-header-content
  .mv-header-main-section-wrapper {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-flow: row wrap;
  flex-flow: row wrap;
  -ms-flex-align: center;
  align-items: center;
  margin-right: 8px;
}
#betfairviz .mv-header-container .mv-secondary-section {
  -ms-flex-item-align: start;
  align-self: flex-start;
  -ms-flex: none;
  flex: none;
}
#betfairviz .mv-header-container .mv-header-content {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-flow: row nowrap;
  flex-flow: row nowrap;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: justify;
  justify-content: space-between;
  width: 100%;
}
#betfairviz .mv-header-container .mv-header-field {
  line-height: 16px;
  display: inline-block;
  padding-top: 2px;
  padding-bottom: 2px;
  margin-right: 8px;
  vertical-align: middle;
}
</style>
"""

GREEN_TICK_PNG = """iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAS5JREFU
OI3VkzFLw0AYhp+LV2pRrJ2l4B9wNUOmYsHJujpLF39AQCiCIBSKVJwd3F10K7iISxQqDuJgK0Ut
peKkRQ0kHDYOIdGkHQp18V2Oj7vn4e7jO3FwLz3GiDYO/DcC5QgARlnfnhO0rPTgDZQjSEx6kcPx
+vNV8ni0xoLcp2WlUY5AOQIZmILDw+oALperZGYzWJ0mN71KtAeurXF1nKJ9PRMRxeGn3mkIA2iu
7TteGtMU8zW4Ww8lw+BaZ4WAAfwnuLZGYWkDI2ug6zqlErQ55L1eiMAnjVVAIznVDyUTy0W5DdD9
uKDvucxn8uRyOW7PJKa5GYP9fKmf/oi9y2RkEhfnTIzsTljH4XgGBqne3cXqbI0EA0jlDg6j9VAN
ZcP2f0dUzlP//DN9A07KmLe0fWRJAAAAAElFTkSuQmCC"""

GREY_TICK_PNG = """iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAOFJREFU
OI3Fkz+OglAQhz90i2eHF+AcJDQQOu08BQWd27ONlnoQLsARKKheR6ieBYlP4naS0LiVZpOn+C/R
KSf5vvxmJmMlSXLkhRq8Ar9f0LYHlFLPCdr2gNY7wjBkqzfn/tcj8Gq9YmyPsW2boijMBGVZ8rvf
H/vgqqqQUpojbPWGOI4RI2GdJJfgNE3pus4UTCczPM9jsVgiRsJSSt2EAYa+7/8A1HWNEALHcQiC
AK018+95L2wsMcsyAFzXJYoigF7YWOJJkuf5XbCR4L+kaRqklL3wVQFwvvOt+vwz/QEVoIxII0Qr
+gAAAABJRU5ErkJggg=="""

DEPTH_TO_WIDTH_MAP = {
    3: '8%',
    4: '16%',
    5: '24%'
}


class Style(Enum):
    DEFAULT = 'default'
    RAW = 'raw'


def _create_market_book_button(
        selection_id: int,
        market_book: Union[Dict[str, Any], MarketBook],
        side: Side,
        depth: int) -> str:
    if type(market_book) != dict:
        market_book = market_book._data
    html = f'<button class="{side.value.lower()} mv-bet-button ng-isolate-scope {side.value.lower()}{"-selection" if depth == 0 else ""}-button">'
    runner_book = get_runner_book_from_market_book(market_book, selection_id=selection_id, return_type=dict)
    if runner_book:
        available = runner_book.get('ex', {}).get(side.ex_key, [])
        if len(available) >= depth + 1:
            html += f'<span class="bet-button-price">{round(available[depth]["price"], 2)}</span>'
            html += f'<span class="bet-button-size">£{round(available[depth]["size"], 2)}</span>'
    html += '</button>'

    return html


def _create_market_book_table(
        market_book: Union[Dict[str, Any], MarketBook],
        depth: int = 3,
        show_runner_names: bool = True) -> str:
    if type(market_book) != dict:
        market_book = market_book._data
    selection_count = sum(1 for r in market_book['marketDefinition']['runners'] if r['status'] != 'REMOVED')
    publish_time_as_datetime = datetime.datetime.utcfromtimestamp(market_book['publishTime'] / 1000)
    market_time_as_datetime = datetime.datetime.strptime(market_book['marketDefinition']['marketTime'], '%Y-%m-%dT%H:%M:%S.%fZ')

    if market_book['totalMatched'] is None:
        total_matched = '-'
    elif market_book['totalMatched'] == 0:
        # If this is zero, it may be genuinely 0 or it may be historic data
        total_matched = f'{round(calculate_total_matched(market_book), 2):,.2f}'
    else:
        total_matched = f'{market_book["totalMatched"]:,}'

    if publish_time_as_datetime < market_time_as_datetime:
        relative_time_string = f'{market_time_as_datetime - publish_time_as_datetime} until marketTime'
    else:
        relative_time_string = f'{publish_time_as_datetime - market_time_as_datetime} since marketTime'
    if 'eventName' in market_book['marketDefinition']:
        title = market_book['marketDefinition']['eventName']
        if 'name' in market_book['marketDefinition']:
            title += ' - ' + market_book['marketDefinition']['name']
    else:  # handle self recorded data
        venue_or_market_id = market_book['marketDefinition']['venue'] if 'venue' in market_book['marketDefinition'] else market_book['marketId']
        market_type = market_book['marketDefinition']['marketType'].replace('_', ' ').title()
        suffix = 'trnshddt'[0xc0006c000000006c >> 2 * market_time_as_datetime.day & 3::4]
        title = f'{venue_or_market_id} {market_time_as_datetime.day}{suffix} {market_time_as_datetime:%b} - {market_type}'
    html = f"""
        <div id="betfairviz">
        <div class="sports-header-container">
            <div class="sports">
                <div class="bf-col-15-24">
                    <span class="title" style="padding-left: 0px;">
                        {title}
                    </span>
                    <div>
                        <span class="date ng-binding ng-scope">
                            {publish_time_as_datetime}: {relative_time_string} 
                        </span>
                    </div>
                    <div>
                        <span class="date ng-binding ng-scope">
                            Market is {market_book['marketDefinition']['status']}
                        </span>
                    </div>
                </div>
                <div class="bf-col-9-24">
                </div>
            </div>
        </div>
        <div class="mv-header-container">
            <div class="mv-header-content">
                <div class="mv-header-main-section-wrapper">
                    <div class="market-status mv-header-field market-going-inplay">
                        <img src="data:image/png;base64, {GREEN_TICK_PNG if market_book['inplay'] else GREY_TICK_PNG}" style="float: left;">
                        <span class="market-status-label" style="{'color: #090;' if market_book['inplay'] else ''}">
                            {'In-Play' if market_book['inplay'] else 'Going In-Play'}
                        </span>
                    </div>
                </div>
                <div class="mv-secondary-section">
                    <div class="mv-header-total-matched-wrapper">
                        <div class="market-matched mv-header-field">
                            <span class="total-matched-label">Matched:</span>
                            <span class="total-matched">GBP {total_matched}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <table class="runners-header">
            <thead>
                <tr class="rh-line without-lay">
                    <th class="rh-runner-name-header">
                        <span class="rh-selections-count-label ng-binding ng-scope">
                            {selection_count} selections
                        </span>
                    </th>
                    <th class="rh-book-percentage rh-back-book-percentage ng-scope"
                        style="width: {DEPTH_TO_WIDTH_MAP[depth]}">
                        {round(calculate_book_percentage(market_book, Side.BACK) * 100, 1)}%
                    </th>
                    <th class="rh-select-all-buttons rh-select-back-all-button ng-scope">
                    </th>
                    <th class="rh-select-all-buttons ng-scope">
                    </th>
                    <th class="rh-book-percentage rh-lay-book-percentage ng-scope"
                        style="width: {DEPTH_TO_WIDTH_MAP[depth]}">
                        {round(calculate_book_percentage(market_book, Side.LAY) * 100, 1)}%
                    </th>
                </tr>
            </thead>
        </table>
    """
    html += """
        <div class="marketview-list-runners-component bf-row"><div class="runners-container bf-col-24-24">
        <table class="mv-runner-list">
    """
    for runner in market_book['marketDefinition']['runners']:
        tokens = [str(runner['id'])]
        if show_runner_names and 'name' in runner:
            tokens.append(runner['name'])
        if runner['status'] == 'REMOVED':
            tokens.append('Non Runner')
        elif runner['status'] == 'WINNER':
            tokens.append('Winner')
        runner_name = ' - '.join(tokens)
        html += ''
        html += f"""
        <tr class="runner-line ng-scope">
            <td class="runner-data-container without-race-card-info">
                <div class="market-graph-container"></div>
                <div>
                    <div class="runner-info">
                        <div class="default name ng-scope">
                            <h3 class="runner-name ng-binding">
                                {runner_name}
                            </h3>
                        </div>
                    </div>
                </div>
            </td>
        """
        for i in range(depth - 1, -1, -1):
            html += '<td class="bet-buttons">'
            html += _create_market_book_button(runner['id'], market_book, Side.BACK, i)
            html += '</td>'
        for i in range(depth):
            html += '<td class="bet-buttons">'
            html += _create_market_book_button(runner['id'], market_book, Side.LAY, i)
            html += '</td>'
        html += '</tr>'
    html += '</table></div></div></div>'
    return html


def _create_runner_book_table(runner_book: Union[Dict[str, Any], RunnerBook], runner_name: Optional[str] = None) -> str:
    if type(runner_book) is dict:
        price_to_atb = {price_size['price']: f"£{round(price_size['size'], 2)}" for price_size in runner_book['ex']['availableToBack']}
        price_to_atl = {price_size['price']: f"£{round(price_size['size'], 2)}" for price_size in runner_book['ex']['availableToLay']}
        price_to_trd = {price_size['price']: f"£{round(price_size['size'], 2)}" for price_size in runner_book['ex']['tradedVolume']}
        selection_id = runner_book['selectionId']
    else:
        price_to_atb = {price_size.price: f'£{round(price_size.size, 2)}' for price_size in runner_book.ex.available_to_back}
        price_to_atl = {price_size.price: f'£{round(price_size.size, 2)}' for price_size in runner_book.ex.available_to_lay}
        price_to_trd = {price_size.price: f'£{round(price_size.size, 2)}' for price_size in runner_book.ex.traded_volume}
        selection_id = runner_book.selection_id
    title = selection_id if runner_name is None else runner_name
    all_prices = sorted(set(itertools.chain(price_to_atb.keys(), price_to_atl.keys(), price_to_trd.keys())))
    html = f"""
    <div id="betfairviz">
        <table class="ladder-table" cellspacing="0">
            <thead>
                <tr class="titles">
                    <th class="exchange-traded ng-scope" colspan=4>{title}</th>
                </tr>
                <tr class="headers">
                    <th class="price ng-scope">Price</th>
                    <th class="back ng-scope">To Back</th>
                    <th class="lay ng-scope">To Lay</th>
                    <th class="trader ng-scope">Traded</th>
                </tr>
            </thead>
            <tbody>"""
    for price in all_prices:
        html += f"""
                <tr class="item ng-scope">
                <td class="price{' back-color' if price in price_to_atb else ' lay-color' if price in price_to_atl else ''}">{round(price, 2)}</td>
                <td class="back{' back-color' if price in price_to_atb else ''}">{price_to_atb.get(price, '')}</td>
                <td class="lay{' lay-color' if price in price_to_atl else ''}">{price_to_atl.get(price, '')}</td>
                <td class="traded">{price_to_trd.get(price, '')}</td>
                </tr>
        """
    html += """
            </tbody>
        </table>
    </div>
    """
    return html


def _create_market_book_html(
        market_book: Union[Dict[str, Any], MarketBook],
        depth: int = 3,
        show_runner_names: bool = True) -> str:
    if type(market_book) != dict:
        market_book = market_book._data
    return CSS_STYLE + _create_market_book_table(market_book, depth=depth, show_runner_names=show_runner_names)


def _create_runner_book_html(runner_book: Union[Dict[str, Any], RunnerBook], runner_name: Optional[str] = None) -> str:
    return CSS_STYLE + _create_runner_book_table(runner_book, runner_name=runner_name)


def visualise(
        market_book_or_runner_book: Union[Dict[str, Any], MarketBook, RunnerBook],
        depth: int = 3,
        show_runner_names: bool = True,
        runner_name: Optional[str] = None,
        style: Union[str, Style] = Style.DEFAULT) -> Union[HTML, Pretty]:
    if (5 < depth) or (depth < 3):
        raise ValueError(f'depth = {depth} is unsupported. Valid values are 3, 4 and 5')
    if type(style) is str:
        style = Style(style)

    if is_market_book(market_book_or_runner_book):
        market_book = market_book_or_runner_book
        if style is Style.DEFAULT:
            return HTML(
                _create_market_book_html(market_book=market_book, depth=depth, show_runner_names=show_runner_names)
            )
        elif style is Style.RAW:
            return Pretty(pretty(market_book))
        else:
            raise ValueError(f'Unrecognised style: {style}')
    elif is_runner_book(market_book_or_runner_book):
        runner_book = market_book_or_runner_book
        if style is Style.DEFAULT:
            return HTML(_create_runner_book_html(runner_book=runner_book, runner_name=runner_name))
        elif style is Style.RAW:
            return Pretty(pretty(runner_book))
        else:
            raise ValueError(f'Unrecognised style: {style}')
    else:
        raise TypeError(f'market_book_or_runner_book is neither a market book nor a runner book')


visualize = visualise


def _dict_formatter(d: dict) -> str:
    if is_market_book(d):
        return _create_market_book_html(d)
    if is_runner_book(d):
        return _create_runner_book_html(d)


ip = get_ipython()
if ip:
    ip.display_formatter.formatters['text/html'].for_type(
        MarketBook,
        _create_market_book_html
    )
    ip.display_formatter.formatters['text/html'].for_type(
        RunnerBook,
        _create_market_book_html
    )
    ip.display_formatter.formatters['text/html'].for_type(
        dict,
        _dict_formatter
    )
