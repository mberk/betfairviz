import itertools
from enum import Enum
from html import escape
from typing import Any, Dict, Union

from betfairlightweight.resources.bettingresources import MarketBook
from betfairlightweight.resources.bettingresources import RunnerBook
from IPython import get_ipython
from IPython.display import HTML
from IPython.display import Pretty
from IPython.lib.pretty import pretty

from betfairutil import is_market_book
from betfairutil import is_runner_book

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
    'totalMatched': None,
    'version': 3342028375
}

EXAMPLE_RUNNER_BOOK = EXAMPLE_MARKET_BOOK['runners'][0]

CSS_STYLE = """
<style>
html {
  color: #000;
  background: #fff;
}
blockquote,
body,
code,
dd,
div,
dl,
dt,
fieldset,
form,
h1,
h2,
h3,
h4,
h5,
h6,
input,
legend,
li,
ol,
p,
pre,
td,
textarea,
th,
ul {
  margin: 0;
  padding: 0;
  line-height: 1;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
fieldset,
img {
  border: 0;
}
address,
caption,
cite,
code,
dfn,
em,
strong,
th,
var {
  font-style: normal;
  font-weight: 400;
}
li {
  list-style: none;
}
caption,
th {
  text-align: left;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-size: 100%;
  font-weight: 400;
}
q::after,
q::before {
  content: "";
  content: none;
}
abbr,
acronym {
  border: 0;
  font-variant: normal;
}
sup {
  vertical-align: text-top;
}
sub {
  vertical-align: text-bottom;
}
input,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
}
legend {
  color: #000;
}
button {
  border-radius: 0;
}
.front-pages {
  background: #dfe5e5;
}
@keyframes highlightBack {
  0% {
    background-color: #54b3ff;
  }
  50% {
    background-color: #ff0;
  }
  100% {
    background-color: #54b3ff;
  }
}
@keyframes highlightLay {
  0% {
    background-color: #f996ab;
  }
  50% {
    background-color: #ff0;
  }
  100% {
    background-color: #f996ab;
  }
}
@keyframes highlightGrey {
  0% {
    background-color: #e3e8e8;
  }
  50% {
    background-color: #ff0;
  }
  100% {
    background-color: #e3e8e8;
  }
}
.hidden {
  display: none;
}
.not-visible {
  visibility: hidden;
}
.bf-row {
  line-height: 0;
}
[ng-controller] {
  line-height: inherit;
}
.left-side-column {
  float: left;
}
#main-wrapper .center-column,
#main-wrapper .left-side-column {
  border-right: 1px solid #bfbfbf;
}
#main-wrapper .center-column {
  overflow: visible;
}
.right-side-column {
  position: relative;
  height: 100%;
}
.default-min-size-page {
  min-width: 1024px;
  min-height: 600px;
}
.pop-out-live-stream-container {
  background-color: #000;
}
.grid-container {
  width: 1024px;
  margin: 0 auto;
}
.main-container .main-content,
.main-container .navigation,
.main-container .right-content {
  float: left;
}
.main-container .navigation {
  min-height: 350px;
  width: 174px;
  background-color: #fff;
  border-right: 1px solid rgba(0, 0, 0, 0.25);
  position: relative;
}
.main-container .main-content {
  width: 512px;
}
.main-container .right-content {
  border-left: 1px solid rgba(127, 127, 127, 0.55);
  overflow-x: hidden;
  background-color: #fff;
  position: relative;
}
.main-container .right-content-bottom {
  position: absolute;
  bottom: 0;
  width: 100%;
}
.generic-submit-btn {
  display: block;
  cursor: pointer;
  margin-right: 8px;
  padding: 6px 8px;
  border: 0;
  outline: 0;
  border-radius: 2px;
  text-align: center;
  font-weight: 700;
  color: #1e1e1e;
  background-color: #ffb80c;
}
.generic-submit-btn:active {
  border: 0;
  box-shadow: inset 1px 2px 2px 0 rgba(0, 0, 0, 0.25);
}
.generic-submit-btn:hover {
  background-color: #e5a50b;
}
.generic-submit-btn:disabled {
  cursor: no-drop;
  background-color: #ffdc86;
  color: #a8915b;
}
.betslip-cancel-btn {
  display: block;
  cursor: pointer;
  margin-right: 8px;
  padding: 6px 10px 7px;
  border-radius: 2px;
  text-align: center;
  font-weight: 700;
  color: #1e1e1e;
  background-color: #cbcbcb;
  border: 0;
}
.betslip-submit-btn {
  display: block;
  cursor: pointer;
  margin-right: 8px;
  padding: 6px 10px 7px;
  border-radius: 2px;
  text-align: center;
  font-weight: 700;
  color: #1e1e1e;
  background-color: #ffb900;
  border: 0;
}
.betslip-cancel-btn.disabled,
.betslip-submit-btn.disabled {
  opacity: 0.5;
  cursor: no-drop;
}
@media only screen and (min-width: 1024px) and (max-width: 1280px) {
  .grid-container {
    width: 100%;
  }
}
@media only screen and (min-width: 1279px) and (max-width: 1440px) {
  .grid-container {
    width: 100%;
  }
}
@media only screen and (min-width: 1439px) and (max-width: 1600px) {
  .grid-container {
    width: 100%;
  }
}
@media only screen and (min-width: 1600px) {
  .grid-container {
    width: 100%;
  }
  .main-container .right-content {
    width: 438px;
    min-width: 438px;
  }
}
.ie10 .bf-tooltip {
  display: block;
}
.icon {
  display: inline-block;
  margin-top: 0;
  line-height: 16px;
  text-align: text-top;
}
.icon.cherry-icon {
  width: 14px;
  height: 16px;
  margin: 6px 6px 0 0;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1154px;
  background-color: transparent;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.generic-tabs-container {
  width: 100%;
  float: left;
  clear: left;
  height: 28px;
  border-bottom: 1px solid #dfdfdf;
  background-color: #efefef;
}
.generic-tabs-container li {
  position: relative;
}
.generic-tabs-container .generic-tab {
  cursor: pointer;
  float: left;
  border-right: 1px solid #dfdfdf;
  border-left: 1px solid #dfdfdf;
  margin-left: -1px;
  display: block;
  height: 26px;
  line-height: 26px;
  padding-top: 2px;
  font-weight: 700;
  background-color: #efefef;
  text-decoration: none;
  white-space: nowrap;
}
.generic-tabs-container .generic-tab a,
.generic-tabs-container .generic-tab div {
  padding: 0 16px;
  display: block;
}
.generic-tabs-container .generic-tab:first-child {
  margin-left: 0;
  border-left: 0;
}
.generic-tabs-container .generic-tab:last-child {
  margin-right: 0;
}
.generic-tabs-container .generic-tab-selected {
  position: relative;
  background: #fff;
  padding-top: 2px;
  height: 27px;
}
.generic-tabs-container .generic-tab-selected::before {
  border-top: 2px solid #ffb80c;
  content: "";
  display: block;
  position: absolute;
  left: -1px;
  right: -1px;
  top: 0;
}
.generic-tabs-container .generic-tab-selected:first-child a,
.generic-tabs-container .generic-tab-selected:first-child div {
  padding-left: 16px;
}
.generic-tabs-container .generic-tab-selected:last-child {
  border-right-color: #fff;
}
.generic-tabs-container .generic-tab-selected:first-child {
  border-left-color: #fff;
  margin-left: 0;
}
.generic-tabs-container .generic-tab-not-selected:hover {
  background-color: #e4e4e4;
}
.full-width-page .content-page-row {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: nowrap;
  -ms-flex-flow: row nowrap;
  flex-flow: row nowrap;
}
.full-width-page .content-page-row .bf-row {
  display: block;
}
.full-width-page .content-page-center-column {
  padding: 16px 16px 0;
  width: calc(100% - 291px);
  -ms-flex: 1 1 0;
  flex: 1 1 auto;
}
.full-width-page .content-page-center-column > .bf-row:not(:last-child) {
  margin-bottom: 16px;
}
.full-width-page .content-page-right-column {
  padding: 16px 16px 0 0;
  -ms-flex: 0 0 auto;
  flex: 0 0 auto;
  width: 243px;
}
.full-width-page
  .content-page-right-column
  > .bf-row:not(:last-child)
  section:not(:empty) {
  margin-bottom: 16px;
} /*! layout-manager - v2.0.6 - 2016-11-15 */
#main-wrapper,
.container,
body,
html {
  height: 100%;
}
html {
  font-size: 62.5%;
}
.container {
  padding-right: 0;
  padding-left: 0;
}
.container::before {
  content: " ";
  height: 100%;
  float: left;
}
.scrollable-panes-height-taker {
  position: relative;
  z-index: 1;
  margin-left: -5px;
  margin-right: -5px;
  padding-left: 5px;
}
.full-width-page .scrollable-panes-height-taker {
  margin-left: 0;
  margin-right: 0;
  padding-left: 0;
}
.scrollable-panes-height-taker::after {
  content: " ";
  clear: both;
  display: block;
}
.scrollable-panes-wrapper {
  position: absolute;
  width: 100%;
  height: 100%;
}
.scrollable-panes-wrapper-helper {
  padding-left: 0 !important;
  padding-right: 0 !important;
  display: inline-block !important;
}
.nested-scrollable-panes-wrapper {
  position: absolute;
  width: 100%;
  height: 100%;
}
.scrollable-pane {
  height: 100%;
  overflow: auto;
}
.scrollable-pane-helper {
  overflow: hidden;
}
.nested-scrollable-pane,
.nested-scrollable-pane-parent {
  height: 100%;
  overflow: hidden;
}
.nested-scrollable-pane-parent::before {
  content: " ";
  height: 100%;
  float: left;
}
.height-taker-helper {
  width: 100%;
  box-sizing: border-box;
  padding-left: 5px;
  padding-right: 5px;
  display: block;
}
.fixed-row-parent {
  position: fixed;
  width: inherit;
  height: 100%;
}
.stick-to-bottom {
  position: absolute;
  bottom: 0;
  width: inherit;
}
.title-header {
  padding: 8px;
  background-color: #303030;
  border-radius: 2px 2px 0 0;
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
  overflow: hidden;
  -ms-flex-pack: justify;
  display: -ms-flexbox;
  display: flex;
  height: 28px;
}
.title-header__title {
  color: #fff;
  margin: 6px 17px 3px 8px;
  font-size: 14px;
  font-weight: 700;
  line-height: 1.1;
  -ms-flex: 1 1 0;
  flex: 1 1 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.scrollable-panes-height-taker::before {
  content: "";
}
@keyframes classicHighlightBack {
  0% {
    background-color: #ddf0ff;
  }
  50% {
    background-color: #ff0;
  }
  100% {
    background-color: #ddf0ff;
  }
}
@keyframes classicHighlightLay {
  0% {
    background-color: #fde9ee;
  }
  50% {
    background-color: #ff0;
  }
  100% {
    background-color: #fde9ee;
  }
}
@keyframes classicHighlightGrey {
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
.classic-theme .subnav-wrapper {
  background: #3a505f;
}
.classic-theme .subnav-wrapper .subnav-link {
  border-right: 1px #263a48 solid;
}
.classic-theme .subnav-wrapper .subnav-first .subnav-link {
  border-left: 1px #263a48 solid;
}
.classic-theme .subnav-wrapper .subnav-link.active:hover,
.classic-theme .subnav-wrapper .subnav-link:focus,
.classic-theme .subnav-wrapper .subnav-link:hover {
  background: #4b6271;
}
.classic-theme .subnav-wrapper .subnav-link:active {
  background: #5b7383;
}
.classic-theme .settings-container,
.classic-theme .settings-container .settings-toggle {
  background: #3a505f;
}
.classic-theme .settings-container .settings-toggle.active:hover,
.classic-theme .settings-container .settings-toggle:focus,
.classic-theme .settings-container .settings-toggle:hover {
  background: #4b6271;
}
.classic-theme .settings-container .settings-toggle:active {
  background-color: #5b7383;
}
.classic-theme .settings-container .tab-navigation .tab-list .tab-title.active {
  border-left: 2px solid #7f7f7f;
}
.classic-theme .generic-tabs-container,
.classic-theme .generic-tabs-container .generic-tab {
  background-color: #e9ebec;
}
.classic-theme .generic-tabs-container .generic-tab-not-selected:hover {
  background-color: #e4e4e4;
}
.classic-theme .generic-tabs-container .generic-tab-selected {
  background-color: #fff;
}
.classic-theme .generic-tabs-container .generic-tab-selected::before {
  border-top-color: #7f7f7f;
}
.classic-theme .mod-tabs .tab-container,
.classic-theme .mod-tabs .tabs-container {
  background-color: #e9ebec;
}
.classic-theme .mod-tabs .tab-container:focus,
.classic-theme .mod-tabs .tab-container:hover {
  background-color: #e4e4e4;
}
.classic-theme .mod-tabs .tab-container.active {
  background-color: #fff;
  border-top-color: #7f7f7f;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn {
  padding: 2px 0 4px 1px;
  background-color: #fff;
  border: 1px solid #dfdfdf;
  border-left: 1px solid #fff;
  border-bottom: 1px solid #fff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn:last-child {
  border-left: 1px solid #dfdfdf;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn:hover {
  background-color: #dfdfdf;
  border-left: 1px solid #dfdfdf;
  border-bottom: 1px solid #dfdfdf;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.back.depth-back-1 {
  border-right: 1px solid #fff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.back.back-selection-button,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.sp-back {
  background-color: #ddf0ff;
  border-top: 0;
  padding: 3px 1px 4px;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.sp-back {
  border-right: 1px solid #fff;
  border-left: 1px solid #fff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.back.back-selection-button {
  border-left: 0;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.back.back-selection-button:hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.suspended.sp-back:hover {
  background-color: #a9d9fe;
  border-left: 0;
  border-bottom: 1px solid #fff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.back.back-selection-button.selected,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.sp-back.selected {
  background-color: #a9d9fe;
  box-shadow: inset 0 0 6px 0 rgba(127, 127, 127, 0.8);
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.back-selection-button:hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.sp-back:hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.suspended.back-selection-button:hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.suspended.sp-back:hover {
  background-color: #a9d9fe;
  border-bottom: 1px solid #fff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.sp-lay {
  border-left: 1px solid #fff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-off:nth-child(1),
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-on:nth-child(3),
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.sp-lay {
  background-color: #fde9ee;
  border-right: 0;
  border-top: 0;
  padding: 3px 1px 4px;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-off:nth-child(1).selected,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-on:nth-child(3).selected,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.sp-lay.selected {
  background-color: #fac9d4;
  box-shadow: inset 0 0 6px 0 rgba(127, 127, 127, 0.8);
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-off:nth-child(1):hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-on:nth-child(3):hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.sp-lay:hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.suspended.lay.market-depth-off:nth-child(1):hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.suspended.lay.market-depth-on:nth-child(3):hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.suspended.sp-lay:hover {
  background-color: #fac9d4;
  border-bottom: 1px solid #fff;
  border-left: 1px solid #fff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-on:nth-child(2):hover {
  border-left: 1px solid #fff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.changed {
  -webkit-animation-name: classicHighlightGrey;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: classicHighlightGrey;
  -moz-animation-duration: 0.3s;
  animation-name: classicHighlightGrey;
  animation-duration: 0.3s;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.back-selection-button.changed {
  -webkit-animation-name: classicHighlightBack;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: classicHighlightBack;
  -moz-animation-duration: 0.3s;
  animation-name: classicHighlightBack;
  animation-duration: 0.3s;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-off:nth-child(1).changed,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-on:nth-child(3).changed {
  -webkit-animation-name: classicHighlightLay;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: classicHighlightLay;
  -moz-animation-duration: 0.3s;
  animation-name: classicHighlightLay;
  animation-duration: 0.3s;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .back-all {
  background-color: #ddf0ff;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .back-all.selected,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .back-all.suspended:hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .back-all:hover {
  background-color: #a9d9fe;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .lay-all {
  background-color: #fde9ee;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .lay-all.selected,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .lay-all.suspended:hover,
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .lay-all:hover {
  background-color: #fac9d4;
}
.classic-theme
  .marketview-wrapper.marketview-list-runners-component
  .runner-container-header
  .sp-bets {
  background-color: #e9ebec;
}
.classic-theme
  .bf-sports-market-header-scroll
  .marketview-wrapper.marketview-list-runners-component
  .runner-list
  .runner-item:nth-child(even)
  .btn {
  border-bottom: 1px solid #dfdfdf;
}
.classic-theme
  .bf-sports-market-header-scroll
  .marketview-wrapper.marketview-list-runners-component
  .runner-list
  .runner-item:nth-child(even)
  .btn.back.back-selection-button,
.classic-theme
  .bf-sports-market-header-scroll
  .marketview-wrapper.marketview-list-runners-component
  .runner-list
  .runner-item:nth-child(even)
  .btn.lay.market-depth-off:nth-child(1),
.classic-theme
  .bf-sports-market-header-scroll
  .marketview-wrapper.marketview-list-runners-component
  .runner-list
  .runner-item:nth-child(even)
  .btn.lay.market-depth-on:nth-child(3) {
  border-bottom: 0;
}
.classic-theme .betslip-view .empty-betslip .sbw-multiples,
.classic-theme .sports-header-container .racing .icon-multiples,
.classic-theme .sports-header-container .sports .icon-multiples {
  background: #5b7484;
  color: #fff;
}
.classic-theme .betslip-view .betslip-footer .betslip-submit-btn {
  background: #5b7484;
  color: #fff;
  font-weight: 400;
}
.classic-theme .betslip-view .bet-header.lay-bets-header {
  background-color: #fac9d4;
}
.classic-theme .betslip-view .bet-header.back-bets-header {
  background-color: #a9d9fe;
}
.classic-theme .navigation-container .navigation-title {
  background: #263a48;
  color: #fff;
  border-top: 1px solid #3a4f5f;
}
.classic-theme .navigation-container .navigation-title:hover {
  background-color: #1c2833;
  color: #fff;
}
.classic-theme
  .navigation-container
  .navigation-content
  .top-navigation
  .section.active-section
  .toggle-node.open {
  background-color: #c9ced1;
}
.classic-theme
  .navigation-container
  .navigation-content
  .top-navigation
  .section.toggle-content
  .navigation-link {
  background-color: #e9ebec;
}
.classic-theme
  .navigation-container
  .navigation-content
  .top-navigation
  .section.toggle-content
  .navigation-link:hover {
  background-color: #c9ced1;
}
.classic-theme
  .navigation-extra-links-container
  .bottom-navigation
  .navigation-link.bottom-navigation-link {
  background: #263a48;
  border-top: 1px solid #3a4f5f;
  color: #fff;
}
.classic-theme
  .navigation-extra-links-container
  .bottom-navigation
  .navigation-link.bottom-navigation-link:hover {
  background-color: #1c2833;
  color: #fff;
}
.classic-theme .favourites-container .favourites-title {
  background: #263a48;
  color: #fff;
}
.classic-theme .favourites-container .favourites-title:hover {
  background-color: #1c2833;
  color: #fff;
}
.classic-theme .left-side-column .lhm-collapse {
  background-color: #263a48;
  color: #fff;
}
.classic-theme .left-side-column .lhm-collapse:hover {
  background-color: #1c2833;
  color: #000;
}
.classic-theme .left-side-column.is-collapsed,
.classic-theme .left-side-column.is-collapsed .lhm-action-wrapper {
  background-color: #263a48;
  color: #fff;
}
.classic-theme
  .left-side-column.is-collapsed
  .shortcut-icon-wrapper
  .shortcut-icon {
  fill: #6e8b9e;
}
.classic-theme .left-side-column.is-collapsed .shortcut-icon-wrapper:hover {
  background-color: #5c7484;
}
.classic-theme
  .left-side-column.is-collapsed
  .shortcut-icon-wrapper:hover
  .shortcut-icon:not(.active) {
  fill: #fff;
}
.ie10 .super-coupon header {
  display: -ms-flexbox;
}
.ie10 .marketview-list-runners-component .runner-item .btn.changed {
  transition: background 0.3s ease-in;
  -moz-transition: background 0.3s ease-in;
  -webkit-transition: background 0.3s ease-in;
}
.ie10 .marketview-list-runners-component .runner-item .changed {
  background: #ff0;
}
.ie10 .marketview-list-runners-component .mv-runner-list .runner-line .back,
.ie10 .marketview-list-runners-component .mv-runner-list .runner-line .lay {
  height: 30px;
}
.ie .container.scrollable-columns {
  float: left;
  width: 100%;
  height: 100%;
  position: absolute;
  overflow: hidden;
  padding-left: 0;
  padding-right: 0;
}
.ie .scrollable-columns .scrollable-panes-height-taker {
  margin-left: 0;
  margin-right: -5px;
  padding-left: 0;
}
.ie .full-width-page .scrollable-panes-height-taker {
  margin-right: 0;
}
.ie .scrollable-columns .bf-row {
  margin-left: 0;
  margin-right: 0;
}
.ie .scrollable-columns .bf-row-internal {
  position: relative;
  margin-left: -5px;
  margin-right: -5px;
}
.ie .full-width-page .scrollable-columns .bf-row-internal {
  margin-left: 0;
  margin-right: 0;
}
.load-screen.ng-enter,
.load-screen.ng-leave.ng-leave-active {
  transition: all 500ms ease-out;
  opacity: 0;
}
.load-screen.ng-enter.ng-enter-active,
.load-screen.ng-leave {
  transition: all 500ms ease-out;
  opacity: 1;
}
@keyframes newHighlightBack {
  0% {
    background-color: #a6d8ff;
  }
  50% {
    background-color: #ffff7f;
  }
  100% {
    background-color: #a6d8ff;
  }
}
@keyframes newHighlightLay {
  0% {
    background-color: #fac9d4;
  }
  50% {
    background-color: #ffff7f;
  }
  100% {
    background-color: #fac9d4;
  }
}
@keyframes newHighlightGrey {
  0% {
    background-color: #fff;
  }
  50% {
    background-color: #ffff7f;
  }
  100% {
    background-color: #fff;
  }
}
@font-face {
  font-family: BlockBESmoothRegular;
  src: url(images/app/common/assets/fonts/blockbesmooth-regular-webfont_4627_.eot);
  src: local("☺"),
    url(images/app/common/assets/fonts/blockbesmooth-regular-webfont_4627_.woff)
      format("woff"),
    url(images/app/common/assets/fonts/blockbesmooth-regular-webfont_4627_.ttf)
      format("truetype"),
    url(images/app/common/assets/fonts/blockbesmooth-regular-webfont_4627_.svg#webfontrrTzpoyH)
      format("svg");
  font-weight: 400;
  font-style: normal;
}
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 11px;
}
.ngdialog.ng-modal-popup {
  text-align: center;
  overflow: hidden;
}
.ngdialog.ng-modal-popup::before {
  content: "";
  display: inline-block;
  height: 100%;
  vertical-align: middle;
  margin-right: -0.25em;
}
.ngdialog.ng-modal-popup .ngdialog-overlay {
  background: rgba(17, 17, 17, 0.8);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.ngdialog.ng-modal-popup .ngdialog-content {
  display: inline-block;
  vertical-align: middle;
  position: relative;
  width: 50%;
  background: #fff;
  box-shadow: 4px 3px 40px #000;
  text-align: left;
  color: #444;
}
.ngdialog.ng-modal-popup .ngdialog-content .dialog-title {
  background: #dfdfdf;
  font: 700 14px Arial, Helvetica, sans-serif;
  color: #1e1e1e;
  padding: 0 16px;
  height: 32px;
  line-height: 32px;
  margin: 0;
}
.ngdialog.ng-modal-popup .ngdialog-close {
  position: absolute;
  top: 10px;
  right: 16px;
  cursor: pointer;
  width: 14px;
  height: 14px;
  padding: 2px;
  border-radius: 0;
  background: url(images/app/common/assets/svgs/modal-dialog/close-normal_4627_.svg)
    0 0 no-repeat;
}
.ngdialog.ng-modal-popup .ngdialog-close:hover {
  background: url(images/app/common/assets/svgs/modal-dialog/close-active_4627_.svg)
    0 0 no-repeat;
}
.ngdialog.ng-modal-popup .ngdialog-close::before {
  content: none;
}
.bf-flag {
  height: 100%;
  width: 100%;
}
.bf-select-component {
  position: relative;
  box-sizing: content-box;
  width: 197px;
  border: 1px solid hsl(0, 0%, 87.5%);
  border-radius: 2px;
}
.bf-select-component .selected-option {
  font-size: 11px;
  font-weight: 700;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  position: relative;
  z-index: 2;
  display: block;
  padding: 6px 20px 5px 6px;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  color: hsl(0, 0%, 11.7%);
  background-color: #fff;
}
.bf-select-component .select-component-arrow {
  position: absolute;
  z-index: 3;
  top: 6px;
  right: 6px;
  fill: hsl(0, 0%, 49.7%);
  transform: rotate(-90deg);
  -ms-transform: rotate(-90deg);
  cursor: pointer;
  pointer-events: none;
}
.bf-select-component .options-list {
  position: absolute;
  z-index: 1;
  top: 22px;
  left: -1px;
  display: none;
  width: 197px;
  border: 1px solid hsl(0, 0%, 87.5%);
  border-top-width: 0;
  border-radius: 0 0 2px 2px;
  background-color: #fff;
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.2);
}
.bf-select-component .options-list .option-list-item {
  display: block;
  padding: 5px 6px;
  cursor: pointer;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  color: hsl(0, 0%, 11.7%);
}
.bf-select-component .options-list .option-list-item:hover {
  background-color: hsl(0, 0%, 96.5%);
}
.bf-select-component.expanded {
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.2);
}
.bf-select-component.expanded .select-component-arrow {
  transform: rotate(90deg);
  -ms-transform: rotate(90deg);
}
.bf-select-component.expanded .options-list {
  display: block;
}
.card-header__buttons {
  text-align: right;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
}
.card-header__button {
  color: #1e1e1e;
  border: 0;
  background-color: #bfbfbf;
  display: inline-block;
  height: 28px;
  border-radius: 2px;
  cursor: pointer;
  box-sizing: border-box;
  padding: 8px;
  margin-left: 8px;
  font-size: 12px;
  font-weight: 700;
  text-decoration: none;
}
.card-header__button:first-child {
  margin-left: 0;
}
.card-header__button:hover {
  background-color: #dfdfdf;
}
.card-header__button.is-selected,
.card-header__button.is-selected:hover {
  background-color: #fff;
}
.card-header__button--highlighted {
  color: #fff;
  background-color: #20a052;
}
.card-header__button--highlighted:hover {
  background-color: #1c8c47;
}
.card-header__button--highlighted.is-selected,
.card-header__button--highlighted.is-selected:hover {
  color: #20a052;
  background-color: #fff;
}
.card-header__container {
  padding: 8px;
  background-color: #303030;
  border-radius: 2px 2px 0 0;
  overflow: hidden;
  display: -ms-flexbox;
  display: flex;
  height: 28px;
  -ms-flex-align: center;
  align-items: center;
}
.card-header__title {
  color: #fff;
  margin: auto;
  font-size: 12px;
  font-weight: 700;
  line-height: 1.1;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  white-space: nowrap;
  overflow: visible;
  text-overflow: ellipsis;
}
.card-header__icon {
  height: 12px;
  width: 12px;
  margin: auto 4px auto 0;
}
.card-header__buttons-container {
  display: block;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
}
.mod-cashout .progress-bar {
  transition: width 1s linear;
  -moz-transition: width 1s linear;
  -webkit-transition: width 1s linear;
}
.cashout-help-modal-dialog {
  color: #444;
}
.cashout-help-modal-dialog .dialog {
  width: 600px;
  line-height: 1.4;
}
.cashout-help-modal-dialog .dialog-msg {
  padding: 16px;
}
.cashout-help-modal-dialog .title {
  padding: 0 16px 5px 0;
  border-bottom: 2px solid #273a47;
  font-size: 18px;
  text-decoration: none;
  margin-bottom: 6px;
  font-weight: 700;
}
.cashout-help-modal-dialog .title-cashout-plus {
  margin-top: 20px;
}
.cashout-help-modal-dialog .description,
.cashout-help-modal-dialog .links-bar {
  margin: 4px 0;
}
.cashout-help-modal-dialog .line {
  padding: 5px 0;
}
.cashout-help-modal-dialog .links-bar {
  line-height: 25px;
  text-align: center;
}
.cashout-help-modal-dialog .link {
  color: #2789ce;
  font-weight: 700;
  padding: 0 12px;
  text-decoration: none;
  cursor: pointer;
}
.coupon-page-navigation {
  display: flex;
  display: -ms-flexbox;
  align-items: center;
  -ms-flex-align: center;
  margin-bottom: 16px;
  height: 44px;
  padding: 0 8px;
  border-radius: 2px;
  background-color: #fff;
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
}
.coupon-page-navigation__item {
  font-size: 12px;
}
.coupon-page-navigation__item--bullets {
  margin: 0 auto;
}
.coupon-page-navigation__label {
  cursor: pointer;
}
.coupon-page-navigation__label--first {
  margin: 0 7px 0 2px;
}
.coupon-page-navigation__label--previous {
  margin-left: 2px;
}
.coupon-page-navigation__label--next {
  margin-right: 3px;
}
.coupon-page-navigation__label--last {
  margin: 0 3px 0 6px;
}
.coupon-page-navigation__label:hover {
  text-decoration: underline;
}
.coupon-page-navigation__icon {
  cursor: pointer;
}
.coupon-page-navigation__icon.is-double-left {
  margin-right: -5px;
}
.coupon-page-navigation__icon.is-double-left,
.coupon-page-navigation__icon.is-double-right,
.coupon-page-navigation__icon.is-single {
  width: 9px;
  height: 9px;
  fill: #7f7f7f;
}
.coupon-page-navigation__icon.is-rotated {
  transform: rotate(180deg);
}
.coupon-page-navigation__bullets {
  display: -ms-flexbox;
  display: flex;
}
.coupon-page-navigation__bullet {
  width: 4px;
  height: 4px;
  margin: 0 2px;
  border-radius: 4px;
  background-color: #dfdfdf;
}
.coupon-page-navigation__bullet.is-active {
  background-color: #303030;
}
.coupon-page-navigation__link {
  text-decoration: none;
  color: #303030;
}
.coupon-page-navigation__link.is-disabled,
.coupon-page-navigation__link.is-disabled .coupon-page-navigation__icon,
.coupon-page-navigation__link.is-disabled .coupon-page-navigation__label {
  cursor: default;
}
.coupon-page-navigation__link.is-disabled .coupon-page-navigation__label {
  color: #7f7f7f;
}
.coupon-page-navigation__link.is-disabled .coupon-page-navigation__label:hover {
  text-decoration: none;
}
.coupon-table-mod .coupon-table {
  width: 100%;
}
.coupon-table-mod .coupon-table .bf-bet-button {
  float: left;
  width: 52px;
  height: 42px;
}
.coupon-table-mod .coupon-table .bf-bet-button:first-child {
  margin-right: 1px;
}
.coupon-table-mod .coupon-table .bf-bet-button.back-button.changed {
  -webkit-animation-name: newHighlightBack;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: newHighlightBack;
  -moz-animation-duration: 0.3s;
  animation-name: newHighlightBack;
  animation-duration: 0.3s;
}
.coupon-table-mod .coupon-table .bf-bet-button.lay-button.changed {
  -webkit-animation-name: newHighlightLay;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: newHighlightLay;
  -moz-animation-duration: 0.3s;
  animation-name: newHighlightLay;
  animation-duration: 0.3s;
}
.coupon-table-mod .coupon-table thead {
  background-color: #dfdfdf;
}
.coupon-table-mod .coupon-table thead th {
  font-size: 12px;
  font-weight: 700;
  text-align: center;
  color: #303030;
  padding: 6px 0;
  width: 113px;
  text-indent: -6px;
}
.coupon-table-mod .coupon-table thead th:first-child {
  text-align: left;
  width: auto;
  padding-left: 8px;
  text-indent: 0;
}
.coupon-table-mod .coupon-table thead th.market-rules-table-header {
  width: auto;
}
.coupon-table-mod .coupon-table tbody tr {
  border-top: 1px solid #eee;
}
.coupon-table-mod .coupon-table tbody tr:first-child {
  border-top: 0;
}
.coupon-table-mod .coupon-table tbody tr:first-child .bf-bet-button {
  height: 41px;
  margin-top: 1px;
}
.coupon-table-mod .coupon-table tbody tr:nth-last-child(2) .bf-bet-button {
  height: 41px;
}
.coupon-table-mod
  .coupon-table
  tbody
  tr:nth-of-type(1):nth-last-of-type(2)
  .bf-bet-button {
  height: 40px;
}
.coupon-table-mod .coupon-table tbody td {
  background: #fff;
}
.coupon-table-mod .coupon-table tbody td:first-child {
  width: auto;
  max-width: 0;
}
.coupon-table-mod .coupon-table tbody .coupon-table-loading {
  display: table-row;
  height: 89px;
}
.coupon-table-mod .coupon-table tbody .coupon-table-loading td {
  background: 0 0;
  background-image: url(images/app/common/assets/images/betslip_spinner_4627_.gif);
  background-repeat: no-repeat;
  background-position: center center;
  background-color: #fff;
}
.coupon-table-mod .coupon-table .coupon-runners {
  position: relative;
  white-space: nowrap;
}
.coupon-table-mod .coupon-table .coupon-runner {
  width: 113px;
  display: inline-block;
  height: 40px;
}
.coupon-table-mod .coupon-table .coupon-market-rules {
  width: 16px;
  height: 16px;
  margin: 0 8px;
  padding: 0 8px 0 0;
}
.coupon-table-mod .coupon-table.hide-lays thead td.market-rules-table-header,
.coupon-table-mod .coupon-table.hide-lays thead th.market-rules-table-header {
  width: auto;
}
.coupon-table-mod .coupon-table.hide-lays .coupon-runner {
  width: 61px;
}
.coupon-table-mod
  .coupon-table
  .mod-event-line
  .mini
  .bf-livescores-start-date
  .start-date-wrapper {
  padding: 0 9px;
}
.coupon-table-mod
  .coupon-table
  .mod-event-line
  .bf-livescores.mini
  .bf-livescores-start-date {
  padding: 0;
}
.coupon-table-mod .coupon-table .mod-event-line .bf-tooltip-wrapper {
  border-collapse: separate;
}
.coupon-table-mod .coupon-table .mod-event-line {
  height: 42px;
}
.coupon-table-mod .coupon-table .mod-event-line .bf-livescores.mini {
  height: 42px;
  overflow: hidden;
}
.coupon-table-mod .coupon-table .inline-betting-container.ng-leave {
  transition: all 0.25s linear;
  -moz-transition: all 0.25s linear;
  -webkit-transition: all 0.25s linear;
  opacity: 1;
}
.coupon-table-mod
  .coupon-table
  .inline-betting-container.ng-leave.ng-leave-active {
  opacity: 0;
}
.coupon-table-mod .coupon-table .headers th:first-child .matched {
  margin-right: 30px;
  float: right;
}
.coupon-table-mod .coupon-table .headers th:first-child.medium .matched,
.coupon-table-mod .coupon-table .headers th:first-child.small .matched {
  display: none;
}
.coupon-table-mod .coupon-table .headers th:first-child.large .matched {
  margin-right: 5px;
}
.coupon-table-mod .coupon-table.hide-lays thead td:not(:first-child),
.coupon-table-mod .coupon-table.hide-lays thead th:not(:first-child) {
  width: 61px;
}
.coupon-table-mod .coupon-table tbody tr + tr.coupon-table-loading {
  display: none;
}
.coupon-table-mod .mod-link {
  text-decoration: none;
}
.coupon-table-mod .coupon-state-overlay {
  display: block;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  text-align: center;
}
.coupon-table-mod .coupon-state-overlay .state-overlay-container {
  height: 100%;
  background-color: rgba(255, 255, 255, 0.65);
  border: 2px solid #b30000;
  box-sizing: border-box;
  margin-right: 9px;
}
.coupon-table-mod .coupon-state-overlay .state-overlay-container .state-label {
  font-size: 14px;
  line-height: 39px;
  font-weight: 700;
  color: #b30000;
  text-align: center;
  display: inline-block;
}
.coupon-filter-by {
  float: right;
  height: 24px;
}
.coupon-filter-by__title {
  margin-right: 3px;
}
.coupon-filter-by__option {
  font-size: 11px;
  line-height: 24px;
  font-weight: 700;
  border-radius: 2px;
  margin-left: 4px;
  padding: 5px 9px;
  cursor: pointer;
  color: #7f7f7f;
  background-color: #dfdfdf;
  border: solid 1px #dfdfdf;
}
.coupon-filter-by__option.is-selected,
.coupon-filter-by__option:hover {
  color: #1e1e1e;
  background-color: #fff;
}
.coupon-filter-by__checkbox {
  display: none;
}
.coupon-filter-by__matched-amount {
  margin-left: 4px;
}
.coupon-filter-by__matched-amount .bf-dropdown-icon {
  top: 6px;
  right: 8px;
}
.coupon-filter-by__matched-amount .bf-dropdown-content {
  top: 25px;
  width: 236px;
  z-index: 55;
}
.coupon-filter-by__matched-amount .bf-dropdown-title-container {
  padding: 6px 24px 8px 8px;
  z-index: 55;
  min-width: 91px;
  text-align: center;
  color: #1e1e1e;
  background-color: #fff;
  border: 1px solid #dfdfdf;
  border-bottom-width: 0;
}
.coupon-filter-by__matched-amount .bf-dropdown-title-container.is-collapsed {
  padding-top: 7px;
  padding-bottom: 6px;
  background: #dfdfdf;
  color: #7f7f7f;
}
.coupon-filter-by__matched-amount
  .bf-dropdown-title-container.is-collapsed
  .bf-dropdown-icon {
  top: 7px;
  fill: #7f7f7f;
}
.coupon-filter-by__matched-amount
  .bf-dropdown-title-container.is-collapsed:hover {
  color: #1e1e1e;
  padding: 6px 24px 5px 8px;
  background: #fff;
  border: 1px solid #dfdfdf;
}
.coupon-filter-by__matched-amount
  .bf-dropdown-title-container.is-collapsed:hover
  .bf-dropdown-icon {
  top: 6px;
  right: 8px;
  fill: #1e1e1e;
}
.coupon-filter-by__matched-amount.has-value
  .bf-dropdown-title-container.is-collapsed {
  color: #1e1e1e;
  padding: 6px 24px 5px 8px;
  background: #fff;
  border: 1px solid #dfdfdf;
}
.coupon-filter-by__matched-amount.has-value
  .bf-dropdown-title-container.is-collapsed
  .bf-dropdown-icon {
  top: 6px;
  right: 8px;
  fill: #1e1e1e;
}
.coupon-filter-by__matched-amount-description {
  margin-bottom: 12px;
}
.coupon-filter-by__matched-amount-content {
  margin-bottom: 12px;
  height: 20px;
}
.coupon-filter-by__matched-amount-label {
  float: left;
  font-weight: 700;
  line-height: 20px;
}
.coupon-filter-by__matched-amount-input {
  float: right;
  border: solid 1px #dfdfdf;
  border-radius: 2px;
  text-align: center;
  height: 100%;
  width: 40%;
}
.coupon-filter-by__matched-amount-input:active,
.coupon-filter-by__matched-amount-input:focus {
  outline: -webkit-focus-ring-color auto 3px;
}
.coupon-filter-by__clear-matched-amount {
  text-align: center;
}
.coupon-filter-by__clear-matched-amount-button {
  min-width: 76px;
  height: 28px;
  font-weight: 700;
  background-color: #bfbfbf;
  color: #1e1e1e;
  border: solid 1px #bfbfbf;
  border-radius: 2px;
  outline: 0;
}
.coupon-filter-by__clear-matched-amount-button:hover {
  background-color: #dfdfdf;
  border: solid 1px #dfdfdf;
}
.coupon-title__navigation {
  text-align: right;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
}
.coupon-title__navigation-button {
  display: inline-block;
  margin: 0 0 8px 8px;
}
.coupon-title__navigation-button:first-child {
  margin-left: 0;
}
.bf-dropdown {
  position: relative;
  display: inline-block;
  font-weight: 400;
  font-size: 11px;
}
.bf-dropdown-icon {
  position: absolute;
  top: 7px;
  right: 8px;
  transition: transform 0.2s ease;
  -moz-transition: transform 0.2s ease;
  -webkit-transition: transform 0.2s ease;
  transform: rotate(90deg);
  -ms-transform: rotate(90deg);
}
.bf-dropdown-title-container {
  position: relative;
  z-index: 4;
  padding: 7px 24px 8px 8px;
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  color: #1e1e1e;
  background-color: #fff;
  border: 1px solid #dfdfdf;
  border-bottom-width: 0;
  cursor: pointer;
  border-radius: 2px 2px 0 0;
}
.bf-dropdown-title-container.is-collapsed {
  z-index: 2;
  color: #1e1e1e;
  background-color: #bfbfbf;
  border: 0;
  padding: 8px 25px 8px 9px;
  border-radius: 2px;
}
.bf-dropdown-title-container.is-collapsed.is-disabled {
  padding-right: 9px;
  cursor: default;
  opacity: 0.7;
}
.bf-dropdown-title-container.is-collapsed .bf-dropdown-icon {
  top: 8px;
  right: 9px;
  transform: rotate(-90deg);
  -ms-transform: rotate(-90deg);
}
.bf-dropdown-content {
  z-index: 3;
  position: absolute;
  top: 26px;
  right: 0;
  padding: 12px;
  border: 1px solid #dfdfdf;
  border-radius: 2px 0 2px 2px;
  background-color: #fff;
}
.bf-dropdown-icon.bf-dropdown-icon {
  fill: #1e1e1e;
}
.mod-event-line {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  position: relative;
  height: 48px;
  font-size: 12px;
  line-height: 18px;
  box-sizing: border-box;
  background-color: #fff;
}
.mod-event-line::after {
  content: " ";
  display: table;
  clear: both;
}
.mod-event-line *,
.mod-event-line ::after,
.mod-event-line ::before {
  box-sizing: inherit;
  line-height: inherit;
}
.mod-event-line:hover {
  background-color: #f6f6f6;
}
.mod-event-line .bf-livescores {
  float: left;
  background-color: #f6f6f6;
  width: 60px;
  height: 48px;
}
.mod-event-line .runners {
  -ms-flex: 1;
  flex: 1;
  overflow: hidden;
  font-weight: 700;
}
.mod-event-line .runners .name {
  padding: 0 8px;
  color: #1e1e1e;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.mod-event-line .bet-counters {
  margin-right: 8px;
}
.mod-event-line .bet-counter {
  display: inline-block;
  font-size: 11px;
  line-height: 11px;
  text-align: center;
  margin: 2px 1px;
  border-radius: 2px;
  padding: 2px 4px;
  color: #fff;
  min-width: 27px;
  visibility: hidden;
}
.mod-event-line .bet-counter .bet-counter-indicator,
.mod-event-line .bet-counter .bet-counter-tooltip-count {
  font-weight: 700;
}
.mod-event-line .bet-counter.unmatched {
  background-color: #d54d4d;
}
.mod-event-line .bet-counter.matched {
  background-color: #3ca963;
}
.mod-event-line .bet-counter.visible {
  visibility: visible;
}
.mod-event-line .bet-counter .bf-tooltip .text {
  color: #fff;
}
.mod-event-line .bet-counter .bf-tooltip {
  padding: 2px 4px;
}
.mod-event-line .bet-counter.unmatched .bf-tooltip,
.mod-event-line .bet-counter.unmatched .bf-tooltip::after {
  background-color: #d54d4d;
}
.mod-event-line .bet-counter.matched .bf-tooltip,
.mod-event-line .bet-counter.matched .bf-tooltip::after {
  background-color: #3ca963;
}
.mod-event-line .matched-amount {
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  text-align: right;
  font-size: 11px;
  color: #7f7f7f;
  width: 90px;
}
.mod-event-line .matched-amount-value {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.mod-event-line .icons {
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  padding: 0 8px;
  min-width: 32px;
}
.mod-event-line .icon-live,
.mod-event-line .icon-tv {
  height: 16px;
}
.mod-event-line .icon-tv {
  margin-bottom: 2px;
}
.mod-event-line .icon-live svg,
.mod-event-line .icon-tv svg {
  width: 16px;
  height: 16px;
  display: inline-block;
  fill: gray;
}
.mod-event-line.small .bet-counter {
  display: block;
}
.mod-event-line.medium .matched-amount,
.mod-event-line.small .matched-amount {
  display: none;
}
.mod-event-line.large .matched-amount,
.mod-event-line.medium .matched-amount,
.mod-event-line.small .matched-amount {
  padding-right: 8px;
}
.mod-event-line.large .icons,
.mod-event-line.medium .icons,
.mod-event-line.small .icons {
  display: none;
}
.mod-event-line .bf-livescores.mini .default-template {
  width: 100%;
  height: 47px;
  max-width: 60px;
  overflow: hidden;
}
.mod-event-line .bf-livescores.mini .bf-livescores-start-date {
  padding: 0 9px;
}
.mod-event-line
  .bf-livescores.mini
  .default-template
  .bf-livescores-time-elapsed {
  width: 35px;
  overflow: hidden;
}
.mod-event-line
  .bf-livescores.mini
  .default-template
  .bf-livescores-match-scores
  .scores {
  width: 25px;
}
.mod-event-line
  .bf-livescores.mini
  .default-template
  .bf-livescores-match-scores
  .scores
  .away,
.mod-event-line
  .bf-livescores.mini
  .default-template
  .bf-livescores-match-scores
  .scores
  .home {
  line-height: 18px;
}
.mod-event-line
  .bf-livescores.mini
  .default-template.darts
  .bf-livescores-extended-scores
  .games,
.mod-event-line
  .bf-livescores.mini
  .default-template.darts
  .bf-livescores-match-scores,
.mod-event-line
  .bf-livescores.mini
  .default-template.darts
  .bf-livescores-time-elapsed,
.mod-event-line
  .bf-livescores.mini
  .default-template.tennis
  .bf-livescores-extended-scores
  .games,
.mod-event-line
  .bf-livescores.mini
  .default-template.tennis
  .bf-livescores-match-scores,
.mod-event-line
  .bf-livescores.mini
  .default-template.tennis
  .bf-livescores-time-elapsed,
.mod-event-line
  .bf-livescores.mini
  .default-template.volleyball
  .bf-livescores-extended-scores
  .games,
.mod-event-line
  .bf-livescores.mini
  .default-template.volleyball
  .bf-livescores-match-scores,
.mod-event-line
  .bf-livescores.mini
  .default-template.volleyball
  .bf-livescores-time-elapsed {
  width: 30px;
}
.mod-event-line
  .bf-livescores.mini
  .default-template.darts
  .bf-livescores-extended-scores
  .games
  .away,
.mod-event-line
  .bf-livescores.mini
  .default-template.darts
  .bf-livescores-extended-scores
  .games
  .home,
.mod-event-line
  .bf-livescores.mini
  .default-template.tennis
  .bf-livescores-extended-scores
  .games
  .away,
.mod-event-line
  .bf-livescores.mini
  .default-template.tennis
  .bf-livescores-extended-scores
  .games
  .home,
.mod-event-line
  .bf-livescores.mini
  .default-template.volleyball
  .bf-livescores-extended-scores
  .games
  .away,
.mod-event-line
  .bf-livescores.mini
  .default-template.volleyball
  .bf-livescores-extended-scores
  .games
  .home {
  line-height: 18px;
}
.mod-event-line .bf-livescores.mini .bf-livescores-innings {
  width: 60px;
}
.mod-event-line .bf-livescores.mini .bf-livescores-innings .current-inning {
  padding-top: 3px;
}
.mod-event-line .bet-counter .bf-tooltip-wrapper .bf-tooltip {
  box-shadow: none;
  border-radius: 2px;
  white-space: nowrap;
  text-align: center;
  width: auto;
  bottom: 10px;
}
.mod-event-line .bet-counter .bf-tooltip-wrapper .bf-tooltip .text {
  text-align: center;
}
.mod-event-line .bet-counter .bf-tooltip-wrapper .bf-tooltip::after {
  border: 0;
  transform: translate(5px, -2px) rotate(45deg);
}
.mod-featured-sports {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.4);
  border-radius: 2px;
  overflow: hidden;
  font-size: 12px;
  line-height: 18px;
  box-sizing: border-box;
  background-color: #fff;
}
.mod-featured-sports *,
.mod-featured-sports ::after,
.mod-featured-sports ::before {
  box-sizing: inherit;
  line-height: inherit;
}
.mod-featured-sports .col-1-1 {
  width: 100%;
}
.mod-featured-sports .col-1-2 {
  width: 50%;
}
.mod-featured-sports .col-1-3 {
  width: 33.3333%;
}
.mod-featured-sports .col-2-3 {
  width: 66.6667%;
}
.mod-featured-sports .header-title-container .header-list {
  background-color: #303030;
  border-radius: 2px 2px 0 0;
  overflow: hidden;
}
.mod-featured-sports .events-list > .col-1-1,
.mod-featured-sports .events-list > .col-1-2,
.mod-featured-sports .events-list > .col-1-3,
.mod-featured-sports .events-list > .col-2-3 {
  float: left;
  border-right: 1px solid #efefef;
}
.mod-featured-sports .header-title-container .header-list .col-1-1,
.mod-featured-sports .header-title-container .header-list .col-1-2,
.mod-featured-sports .header-title-container .header-list .col-1-3,
.mod-featured-sports .header-title-container .header-list .col-2-3 {
  font-weight: 700;
  float: left;
  height: 28px;
  padding: 5px 8px 0;
  border-right: 1px solid #efefef;
}
.mod-featured-sports .footer-container .footer-list .col-1-1,
.mod-featured-sports .footer-container .footer-list .col-1-2,
.mod-featured-sports .footer-container .footer-list .col-1-3,
.mod-featured-sports .footer-container .footer-list .col-2-3 {
  float: left;
  text-align: right;
  height: 28px;
  padding: 5px 8px 0;
  border-right: 1px solid #efefef;
}
.mod-featured-sports .events-list > .col-1-1:last-child,
.mod-featured-sports .events-list > .col-1-2:last-child,
.mod-featured-sports .events-list > .col-1-3:last-child,
.mod-featured-sports .events-list > .col-2-3:last-child,
.mod-featured-sports .header-title-container .header-list .col-1-1:last-child,
.mod-featured-sports .header-title-container .header-list .col-1-2:last-child,
.mod-featured-sports .header-title-container .header-list .col-1-3:last-child,
.mod-featured-sports .header-title-container .header-list .col-2-3:last-child {
  border-right-width: 0;
}
.mod-featured-sports .header-title-container .header-list .col-1-1 a,
.mod-featured-sports .header-title-container .header-list .col-1-2 a,
.mod-featured-sports .header-title-container .header-list .col-1-3 a,
.mod-featured-sports .header-title-container .header-list .col-2-3 a {
  color: #fff;
  text-decoration: none;
}
.mod-featured-sports .footer-container .footer-list .col-1-1 a,
.mod-featured-sports .footer-container .footer-list .col-1-2 a,
.mod-featured-sports .footer-container .footer-list .col-1-3 a,
.mod-featured-sports .footer-container .footer-list .col-2-3 a {
  color: #1e1e1e;
  text-decoration: none;
}
.mod-featured-sports .header-title-container .header-list .col-1-1 a:hover,
.mod-featured-sports .header-title-container .header-list .col-1-2 a:hover,
.mod-featured-sports .header-title-container .header-list .col-1-3 a:hover,
.mod-featured-sports .header-title-container .header-list .col-2-3 a:hover {
  text-decoration: underline;
}
.mod-featured-sports .events-list {
  overflow: hidden;
}
.mod-featured-sports .events-list > .col-1-1 > .event-data,
.mod-featured-sports .events-list > .col-1-2 > .event-data,
.mod-featured-sports .events-list > .col-1-3 > .event-data,
.mod-featured-sports .events-list > .col-2-3 > .event-data {
  height: 48px;
  overflow: hidden;
  border-bottom: 1px solid #efefef;
}
.mod-featured-sports .events-list > .col-1-1 > .event-data:hover,
.mod-featured-sports .events-list > .col-1-2 > .event-data:hover,
.mod-featured-sports .events-list > .col-1-3 > .event-data:hover,
.mod-featured-sports .events-list > .col-2-3 > .event-data:hover {
  cursor: pointer;
}
.mod-featured-sports .footer-container .footer-list {
  border-radius: 0 0 2px 2px;
  overflow: hidden;
  border-top: 1px solid #efefef;
  margin-top: -1px;
  background-color: #fff;
}
.mod-featured-sports .footer-container .footer-list .col-1-1:last-child,
.mod-featured-sports .footer-container .footer-list .col-1-2:last-child,
.mod-featured-sports .footer-container .footer-list .col-1-3:last-child,
.mod-featured-sports .footer-container .footer-list .col-2-3:last-child {
  border-right-width: 0;
}
.mod-featured-sports .footer-container .footer-list .col-1-1 a:hover,
.mod-featured-sports .footer-container .footer-list .col-1-2 a:hover,
.mod-featured-sports .footer-container .footer-list .col-1-3 a:hover,
.mod-featured-sports .footer-container .footer-list .col-2-3 a:hover {
  text-decoration: underline;
}
.mod-featured-sports .footer-container .footer-list .icon-arrow {
  margin-left: 5px;
}
.mod-featured-sports .footer-container .footer-list .icon-arrow.is-single {
  width: 9px;
  height: 9px;
  fill: #7f7f7f;
}
.mod-featured-sports .footer-container .footer-list .icon-arrow.is-rotated {
  transform: rotate(180deg);
}
.ah-mv-wrapper .mv-sticky-header,
.ah-mv-wrapper-for-atg-st .mv-sticky-header {
  padding-bottom: 10px;
}
.ah-mv-wrapper .ah-mv-container .ah-scroll-button-wrapper,
.ah-mv-wrapper-for-atg-st .ah-mv-container .ah-scroll-button-wrapper {
  margin: 8px 6px 0;
  overflow: hidden;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-scroll-button-wrapper.ah-scroll-button-wrapper-bottom,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-scroll-button-wrapper.ah-scroll-button-wrapper-bottom {
  margin: 0 6px 6px;
}
.ah-mv-wrapper .ah-mv-container .ah-scroll-button-wrapper .ah-scroll-button,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button {
  border: 0;
  border-radius: 2px;
  display: block;
  height: 18px;
  width: 100%;
  background-color: #efefef;
  text-align: center;
  line-height: 16px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button:focus,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button:focus {
  outline: 0;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button:hover,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button:hover {
  cursor: pointer;
  background-color: silver;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button:active,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button:active {
  box-shadow: inset 2px 2px 2px 0 rgba(0, 0, 0, 0.25);
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button:disabled,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-scroll-button-wrapper
  .ah-scroll-button:disabled {
  background: 0 0;
  background-color: #e1e1e1;
  opacity: 0.5;
  cursor: auto;
}
.ah-mv-wrapper .ah-mv-container .ah-runner-inner-container-header,
.ah-mv-wrapper-for-atg-st .ah-mv-container .ah-runner-inner-container-header {
  box-shadow: 0 0;
  overflow: hidden;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-runner-inner-container-header-wrapper,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-runner-inner-container-header-wrapper {
  display: block;
  margin: 0 7px;
  background-color: #fff;
  padding-bottom: 1px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections {
  border-bottom: 0;
  margin-left: 0;
  height: auto;
  padding: 0;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .ah-line-number,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .ah-line-number {
  font-size: 11px;
  color: #656565;
  text-align: left;
  margin-right: 10px;
  display: inline-block;
  letter-spacing: normal;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .back-to-evens-button,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .back-to-evens-button {
  max-width: 90px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .show-all-lines-toggle,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .show-all-lines-toggle {
  max-width: 80px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .back-to-evens-button,
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .show-all-lines-toggle,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .back-to-evens-button,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .show-all-lines-toggle {
  margin: 0;
  padding: 0 8px;
  border: 0;
  font-size: 11px;
  line-height: 20px;
  height: 20px;
  background: linear-gradient(0deg, #404040, #353535);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#353535", endColorstr="#404040", GradientType=0);
  color: #fff;
  text-align: center;
  border-radius: 2px;
  cursor: pointer;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .back-to-evens-button:hover,
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .show-all-lines-toggle:hover,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .back-to-evens-button:hover,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .show-all-lines-toggle:hover {
  background: linear-gradient(0deg, #333, #2a2a2a);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#2a2a2a", endColorstr="#333", GradientType=0);
  color: #c4c4c4;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .back-to-evens-button:disabled,
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .show-all-lines-toggle:disabled,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .back-to-evens-button:disabled,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .number-selections
  .show-all-lines-toggle:disabled {
  background: 0 0;
  background-color: #969696;
  color: #fff;
  cursor: auto;
  filter: "progid:DXImageTransform.Microsoft.gradient(enabled = false)";
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .selection-header.selection-header-back,
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .selection-header.selection-header-lay,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .selection-header.selection-header-back,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .selection-header.selection-header-lay {
  border-bottom: 0;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-bet-type-label,
.ah-mv-wrapper .ah-mv-container .ah-runner-inner-container-header .ah-label,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-bet-type-label,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-label {
  color: #1e1e1e;
  height: 20px;
  line-height: 20px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-bet-type-label.ah-bet-label-with-one-column,
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-label.ah-bet-label-with-one-column,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-bet-type-label.ah-bet-label-with-one-column,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .ah-label.ah-bet-label-with-one-column {
  text-align: center;
  padding-right: 0;
  padding-left: 0;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .percentage-back-lay-all-container
  .ah-lay-bet-label,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .percentage-back-lay-all-container
  .ah-lay-bet-label {
  text-align: left;
  padding-left: 15px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-runner-inner-container-header
  .percentage-back-lay-all-container
  .ah-back-bet-label,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-runner-inner-container-header
  .percentage-back-lay-all-container
  .ah-back-bet-label {
  text-align: right;
  padding-right: 15px;
}
.ah-mv-wrapper .ah-mv-container .container-for-bet-buttons-and-bsp,
.ah-mv-wrapper-for-atg-st .ah-mv-container .container-for-bet-buttons-and-bsp {
  text-align: right;
}
.ah-mv-wrapper .ah-mv-container .ah-mv-bet-button-container,
.ah-mv-wrapper-for-atg-st .ah-mv-container .ah-mv-bet-button-container {
  display: inline-block;
  height: 30px;
  border-right: 1px solid #dfdfdf;
}
.ah-mv-wrapper .ah-mv-container .ah-mv-bet-button-container:first-child,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-mv-bet-button-container:first-child {
  border-left: 1px solid #dfdfdf;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-mv-bet-button-container:nth-child(n + 2):nth-child(-n + 4),
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-mv-bet-button-container:nth-child(n + 2):nth-child(-n + 4) {
  border-right: 1px solid #dfdfdf;
}
.ah-mv-wrapper .ah-mv-container .ah-mv-bet-button-container .changed,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-mv-bet-button-container
  .changed {
  -webkit-animation-name: newHighlightGrey;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: newHighlightGrey;
  -moz-animation-duration: 0.3s;
  animation-name: newHighlightGrey;
  animation-duration: 0.3s;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-mv-bet-button-container
  .back-selection-button.changed,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-mv-bet-button-container
  .back-selection-button.changed {
  -webkit-animation-name: newHighlightBack;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: newHighlightBack;
  -moz-animation-duration: 0.3s;
  animation-name: newHighlightBack;
  animation-duration: 0.3s;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-mv-bet-button-container
  .lay-selection-button.changed,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-mv-bet-button-container
  .lay-selection-button.changed {
  -webkit-animation-name: newHighlightLay;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: newHighlightLay;
  -moz-animation-duration: 0.3s;
  animation-name: newHighlightLay;
  animation-duration: 0.3s;
}
.ah-mv-wrapper
  .ah-mv-container
  .runner-item:nth-child(even)
  .ah-mv-bet-button-container,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .runner-item:nth-child(even)
  .ah-mv-bet-button-container {
  border-bottom: 1px solid #dfdfdf;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line,
.ah-mv-wrapper-for-atg-st .ah-mv-container .ah-double-line {
  zoom: 1;
  margin: 0 8px;
  list-style-type: none;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line::after,
.ah-mv-wrapper-for-atg-st .ah-mv-container .ah-double-line::after {
  content: ".";
  display: block;
  clear: both;
  overflow: hidden;
  line-height: 0;
  height: 0;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line.show-ah-summary,
.ah-mv-wrapper-for-atg-st .ah-mv-container .ah-double-line.show-ah-summary {
  height: 198px;
  overflow: hidden;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line .runner-item,
.ah-mv-wrapper-for-atg-st .ah-mv-container .ah-double-line .runner-item {
  margin: 0;
  border-bottom: 1px solid #dfdfdf;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line .runner-item .btn,
.ah-mv-wrapper-for-atg-st .ah-mv-container .ah-double-line .runner-item .btn {
  margin: 0;
  border: 0;
  border-left: 1px solid #fff;
  border-bottom: 1px solid #fff;
  height: 30px;
  line-height: 12px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item
  .btn.back.back-selection-button,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item
  .btn.back.back-selection-button {
  border-right: 0;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line .runner-item .btn:focus,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item
  .btn:focus {
  outline: 0;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line .runner-item .btn .price,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item
  .btn
  .price {
  font-weight: 700;
  display: block;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line .runner-item:first-child,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item:first-child {
  margin-top: 3px;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line .runner-item:nth-child(2n),
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item:nth-child(2n) {
  border-bottom: 0;
  margin-bottom: 5px;
  height: 29px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item:nth-child(2n)
  .runner-info,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item:nth-child(2n)
  .runner-info {
  border-bottom: 0;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .runner-data-container,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .runner-data-container {
  height: 15px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .runner-data-container
  .runner-name,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .runner-data-container
  .runner-name {
  line-height: 12px;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line .runner-item.has-pnl .pnl,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .pnl {
  float: none;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .pnl
  .actual-pnl,
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .pnl
  .potential-pnl,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .pnl
  .actual-pnl,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .pnl
  .potential-pnl {
  padding-left: 5px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .ah-mv-bet-button-container,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.has-pnl
  .ah-mv-bet-button-container {
  height: 29px;
}
.ah-mv-wrapper .ah-mv-container .ah-double-line .runner-item.key-line,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.key-line {
  background-color: #d7d7d7;
  border-bottom: 1px solid #d7d7d7;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item.key-line
  .ah-mv-bet-button-container,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.key-line
  .ah-mv-bet-button-container {
  margin-top: 0;
}
.ah-mv-wrapper
  .ah-mv-container
  .runner-item:nth-child(n + 2):nth-child(even)
  .ah-mv-bet-button-container,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .runner-item:nth-child(n + 2):nth-child(even)
  .ah-mv-bet-button-container {
  border-bottom: 1px solid #dfdfdf;
}
.ah-mv-wrapper
  .ah-mv-container
  .runner-item.key-line
  + .runner-item
  .container-for-bet-buttons-and-bsp
  .ah-mv-bet-button-container,
.ah-mv-wrapper
  .ah-mv-container
  .runner-item:nth-child(n + 2):nth-child(odd)
  .ah-mv-bet-button-container,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .runner-item.key-line
  + .runner-item
  .container-for-bet-buttons-and-bsp
  .ah-mv-bet-button-container,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .runner-item:nth-child(n + 2):nth-child(odd)
  .ah-mv-bet-button-container {
  border-top: 1px solid #dfdfdf;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item.key-line
  + .runner-item,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.key-line
  + .runner-item {
  background-color: #d7d7d7;
  border-bottom: 1px solid #d7d7d7;
  margin-bottom: 4px;
}
.ah-mv-wrapper
  .ah-mv-container
  .ah-double-line
  .runner-item.key-line
  + .runner-item
  .ah-mv-bet-button-container,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .ah-double-line
  .runner-item.key-line
  + .runner-item
  .ah-mv-bet-button-container {
  margin-top: 0;
}
.ah-mv-wrapper .ah-mv-container .market-graph-container,
.ah-mv-wrapper-for-atg-st .ah-mv-container .market-graph-container {
  float: left;
  overflow: hidden;
  width: 13px;
  height: 29px;
  padding-left: 2px;
}
.ah-mv-wrapper .ah-mv-container .market-graph-container .market-graph,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .market-graph-container
  .market-graph {
  margin-top: 7px;
  height: 17px;
  width: 100%;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -193px;
}
.ah-mv-wrapper .ah-mv-container .market-graph-container .market-graph:active,
.ah-mv-wrapper .ah-mv-container .market-graph-container .market-graph:hover,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .market-graph-container
  .market-graph:active,
.ah-mv-wrapper-for-atg-st
  .ah-mv-container
  .market-graph-container
  .market-graph:hover {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -208px;
}
@media only screen and (max-width: 1439px) {
  .ah-mv-wrapper
    .ah-mv-container
    .ah-runner-inner-container-header
    .number-selections
    .ah-line-number,
  .ah-mv-wrapper-for-atg-st
    .ah-mv-container
    .ah-runner-inner-container-header
    .number-selections
    .ah-line-number {
    margin-right: 4px;
  }
  .ah-mv-wrapper
    .ah-mv-container
    .ah-runner-inner-container-header
    .number-selections
    .show-all-lines-toggle,
  .ah-mv-wrapper-for-atg-st
    .ah-mv-container
    .ah-runner-inner-container-header
    .number-selections
    .show-all-lines-toggle {
    margin-right: 2px;
    padding: 0 4px;
  }
  .ah-mv-wrapper
    .ah-mv-container
    .ah-runner-inner-container-header
    .number-selections
    .back-to-evens-button,
  .ah-mv-wrapper-for-atg-st
    .ah-mv-container
    .ah-runner-inner-container-header
    .number-selections
    .back-to-evens-button {
    display: inline-block;
    padding: 0 4px;
  }
  .bf-sports-market-header-scroll
    .ah-marketview-wrapper
    .runner-container-header
    .ah-runner-inner-container-header {
    height: 41px;
  }
}
.ah-pnl-table-wrapper {
  letter-spacing: normal;
  margin-left: 6px;
  background-color: #fff;
}
.ah-pnl-table-wrapper .ah-pnl-table-1280-higher {
  display: none;
}
.ah-pnl-table-wrapper .ah-pnl-table-1280-lower {
  display: table;
}
.ah-pnl-table-wrapper .ah-pnl-table {
  background-color: #fff;
  padding-bottom: 8px;
  border-collapse: separate;
  width: 100%;
  min-width: 100%;
  table-layout: fixed;
}
.ah-pnl-table-wrapper .ah-pnl-table .header-label-row {
  width: 86px;
  margin-top: 16px;
  font-size: 12px;
  color: #1e1e1e;
  font-weight: 700;
}
.ah-pnl-table-wrapper .ah-pnl-table .ah-pnl-team {
  background-color: #d9d9d9;
  text-align: center;
  vertical-align: middle;
  color: #303030;
  font-weight: 700;
  height: 18px;
}
.ah-pnl-table-wrapper .ah-pnl-table .empty-pnl {
  height: 62px;
  color: #1e1e1e;
  background-color: #f0f0f0;
  text-align: center;
  vertical-align: middle;
}
.ah-pnl-table-wrapper .ah-pnl-table .empty-pnl.potential {
  height: 18px;
}
.ah-pnl-table-wrapper .ah-pnl-table .bet-label-row,
.ah-pnl-table-wrapper .ah-pnl-table .empty-pnl,
.ah-pnl-table-wrapper .ah-pnl-table .header-label-row {
  letter-spacing: normal;
}
.ah-pnl-table-wrapper .ah-pnl-table .bet-label-cell {
  font-size: 11px;
  color: #1e1e1e;
  text-align: left;
  vertical-align: middle;
  height: 26px;
}
.ah-pnl-table-wrapper .ah-pnl-table .bet-label-cell-1280-lower {
  text-align: center;
}
.ah-pnl-table-wrapper .ah-pnl-table .ah-pnl-handicap {
  vertical-align: middle;
  text-align: center;
  height: 20px;
}
.ah-pnl-table-wrapper
  .ah-pnl-table
  .ah-pnl-handicap.ah-pnl-handicap-1280-lower {
  border-bottom: 1px solid #d9d9d9;
}
.ah-pnl-table-wrapper .ah-pnl-table .ah-pnl-value {
  vertical-align: middle;
  text-align: center;
  background-color: #f0f0f0;
  color: #060;
  height: 26px;
  border-right: 1px solid #fff;
}
.ah-pnl-table-wrapper .ah-pnl-table .ah-pnl-value .negative-pnl {
  color: #b30000;
}
.ah-pnl-table-wrapper .ah-pnl-table .ah-draw-handicap,
.ah-pnl-table-wrapper .ah-pnl-table .ah-pnl-draw {
  border-left: 1px solid #d9d9d9;
  border-right: 1px solid #d9d9d9;
}
@media only screen and (min-width: 1280px) {
  .ah-pnl-table-wrapper .ah-pnl-table .header-label-row {
    width: 16%;
    min-width: 16%;
  }
}
@media only screen and (min-width: 1440px) {
  .ah-pnl-table-wrapper .ah-pnl-table-1280-higher {
    display: table;
  }
  .ah-pnl-table-wrapper .ah-pnl-table-1280-lower {
    display: none;
  }
}
.st-onboarding-step-other-markets,
bf-atg-st-marketview {
  background: transparent
    url(images/app/common/assets/svgs/onboarding/onboarding-st-other-markets_4627_.svg)
    0 0 no-repeat;
  width: 480px;
  height: 82px;
  margin-top: 10px;
}
.tooltip-step-modal {
  display: table;
}
.mv-sticky-header-atg-st .rh-selections-count-label {
  color: #7f7f7f;
}
.mv-sticky-header-atg-st
  .marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container {
  padding: 8px;
}
.mv-sticky-header-atg-st .market-rotator-container {
  padding: 0 8px;
  background-color: #f6f6f6;
  border-top: 1px solid #dfdfdf;
  border-bottom: 1px solid #dfdfdf;
}
.mv-sticky-header-atg-st .market-rotator {
  width: 48%;
  margin-left: auto;
}
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .mv-sticky-header-atg-st .market-rotator-container {
    margin-right: -17px;
    padding-right: 17px;
  }
}
@supports (-ms-ime-align: auto) {
  .mv-sticky-header-atg-st .market-rotator-container {
    margin-right: -12px;
    padding-right: 12px;
  }
}
.atg-st-pnl-table {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  font-size: 12px;
  padding: 8px;
  border-top: 1px solid #dfdfdf;
}
.atg-st-pnl-table__labels {
  width: 200px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 0 0 200px;
  flex: 0 0 200px;
  -ms-flex-flow: column;
  flex-flow: column;
  -ms-flex-pack: end;
  justify-content: flex-end;
}
.atg-st-pnl-table__label {
  line-height: 26px;
  font-size: 11px;
  color: #303030;
  overflow: hidden;
  text-overflow: ellipsis;
}
.atg-st-pnl-table__rotator-icon--right {
  transform: rotate(180deg);
}
.atg-st-pnl-table__rotator-button {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 0 0 15px;
  flex: 0 0 15px;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
  background: #f6f6f6;
  border: 1px solid #dfdfdf;
  outline: 0;
  padding: 0;
}
.atg-st-pnl-table__rotator-button .atg-st-pnl-table__rotator-icon--left,
.atg-st-pnl-table__rotator-button .atg-st-pnl-table__rotator-icon--right {
  fill: #303030;
}
.atg-st-pnl-table__rotator-button:hover .atg-st-pnl-table__rotator-icon--left,
.atg-st-pnl-table__rotator-button:hover .atg-st-pnl-table__rotator-icon--right {
  fill: #7f7f7f;
}
.atg-st-pnl-table__rotator-button:disabled
  .atg-st-pnl-table__rotator-icon--left,
.atg-st-pnl-table__rotator-button:disabled
  .atg-st-pnl-table__rotator-icon--right {
  fill: #dfdfdf;
}
.atg-st-pnl-table__rotator-button--left {
  border-right: 0;
}
.atg-st-pnl-table__rotator-button--right {
  border-left: 0;
}
.atg-st-pnl-table__table-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  min-width: 0;
  border-left: 1px solid #e1e6ea;
}
.atg-st-pnl-table__item-label--pnl {
  color: #3ca963;
  font-weight: 700;
}
.atg-st-pnl-table__item-label--negative {
  color: #d54d4d;
}
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .atg-st-pnl-table {
    display: -ms-flexbox;
    -ms-flex: 1 1 auto;
  }
  .atg-st-pnl-table__labels {
    display: -ms-flexbox;
    -ms-flex: 0 0 200px;
    -ms-flex-flow: column;
  }
  .atg-st-pnl-table_label {
    display: inline-block;
    width: 100%;
  }
  .atg-st-pnl-table__rotator-button {
    display: -ms-flexbox;
    -ms-flex: 0 0 15px;
    -ms-flex-align: center;
    -ms-flex-pack: center;
  }
  .atg-st-pnl-table__table-container {
    display: -ms-flexbox;
    -ms-flex: 1 1 auto;
  }
}
.atg-st-pnl-table__table--no-header {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  -ms-flex-flow: column;
  flex-flow: column;
}
.atg-st-pnl-table__item-label--no-header {
  height: 26px;
  line-height: 26px;
  text-align: center;
  border-right: 1px solid #e1e6ea;
  box-sizing: border-box;
  padding: 0 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.atg-st-pnl-table__item-label--no-header.atg-st-pnl-table__item-label--handicap {
  border-top: 1px solid #e1e6ea;
}
.atg-st-pnl-table__item-label--no-header.atg-st-pnl-table__item-label--pnl {
  border-bottom: 1px solid #e1e6ea;
}
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .atg-st-pnl-table__table--no-header {
    display: -ms-flexbox;
    -ms-flex: 1 1 100%;
    -ms-flex-flow: column;
    width: 100%;
  }
  .atg-st-pnl-table__item-label--no-header {
    display: inline-block;
  }
}
.atg-st-pnl-table__table-container--with-header {
  border-left: 0;
}
.atg-st-pnl-table__table--with-header {
  width: 100%;
  text-align: center;
  table-layout: fixed;
  border: 1px solid #e1e6ea;
}
.atg-st-pnl-table__header {
  height: 18px;
  background: #f6f6f6;
}
.atg-st-pnl-table__header-label {
  font-size: 11px;
  font-weight: 700;
  color: #303030;
  border: 1px solid #e1e6ea;
}
.atg-st-pnl-table__header-label--draw {
  border-width: 1px 2px;
}
.atg-st-pnl-table__row {
  height: 20px;
}
.atg-st-pnl-table__item-label--with-header {
  border-bottom: 0;
  border-right: 1px solid #e1e6ea;
}
.atg-st-pnl-table__item-label--draw {
  border-left: 1px solid #e1e6ea;
  border-width: 1px 2px;
}
.atg-st-pnl-table__element,
.atg-st-pnl-table__header-label {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 0 4px;
}
.atg-st-pnl-table-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  font-size: 12px;
  padding: 8px;
  border-top: 1px solid #dfdfdf;
}
.atg-st-pnl-table-container .atg-st-pnl-table-labels-container {
  width: 200px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 0 0 200px;
  flex: 0 0 200px;
  -ms-flex-flow: column;
  flex-flow: column;
  -ms-flex-pack: end;
  justify-content: flex-end;
}
.atg-st-pnl-table-container .atg-st-pnl-table-label {
  line-height: 26px;
  font-size: 11px;
  color: #303030;
  overflow: hidden;
  text-overflow: ellipsis;
}
.atg-st-pnl-table-container .atg-st-pnl-table-rotator-left-icon,
.atg-st-pnl-table-container .atg-st-pnl-table-rotator-right-icon {
  fill: #303030;
}
.atg-st-pnl-table-container .atg-st-pnl-table-rotator-right-icon {
  transform: rotate(180deg);
}
.atg-st-pnl-table-container .atg-st-pnl-rotator-button {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 0 0 15px;
  flex: 0 0 15px;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
  background: #f6f6f6;
  border: 1px solid #dfdfdf;
  outline: 0;
  padding: 0;
}
.atg-st-pnl-table-container
  .atg-st-pnl-rotator-button:hover
  .atg-st-pnl-table-rotator-left-icon,
.atg-st-pnl-table-container
  .atg-st-pnl-rotator-button:hover
  .atg-st-pnl-table-rotator-right-icon {
  fill: #7f7f7f;
}
.atg-st-pnl-table-container .atg-st-pnl-rotator-button:disabled {
  cursor: default;
}
.atg-st-pnl-table-container
  .atg-st-pnl-rotator-button:disabled
  .atg-st-pnl-table-rotator-left-icon,
.atg-st-pnl-table-container
  .atg-st-pnl-rotator-button:disabled
  .atg-st-pnl-table-rotator-right-icon {
  fill: #dfdfdf;
}
.atg-st-pnl-table-container .atg-st-pnl-left-rotator {
  border-right: 0;
}
.atg-st-pnl-table-container .atg-st-pnl-right-rotator {
  border-left: 0;
}
.atg-st-pnl-table-container .atg-st-pnl-table-content-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  min-width: 0;
  border-left: 1px solid #e1e6ea;
}
.atg-st-pnl-table-container .atg-st-pnl-table-pnl {
  color: #3ca963;
  font-weight: 700;
}
.atg-st-pnl-table-container .atg-st-pnl-table-pnl.negative {
  color: #d54d4d;
}
.ie .atg-st-pnl-table-container {
  display: -ms-flexbox;
  -ms-flex: 1 1 auto;
}
.ie .atg-st-pnl-table-container .atg-st-pnl-table-labels-container {
  display: -ms-flexbox;
  -ms-flex: 0 0 200px;
  -ms-flex-flow: column;
}
.ie .atg-st-pnl-table-container .atg-st-pnl-table-label {
  display: inline-block;
  width: 100%;
}
.ie .atg-st-pnl-table-container .atg-st-pnl-rotator-button {
  display: -ms-flexbox;
  -ms-flex: 0 0 15px;
  -ms-flex-align: center;
  -ms-flex-pack: center;
}
.ie .atg-st-pnl-table-container .atg-st-pnl-table-content-container {
  display: -ms-flexbox;
  -ms-flex: 1 1 auto;
}
.lm-marketview-list-runners-component .bet-buttons {
  border: 1px solid #dfdfdf;
}
.lm-marketview-list-runners-component .bet-buttons:last-child {
  border-right: 0;
}
.lm-marketview-list-runners-component .bet-buttons button,
.lm-marketview-list-runners-component .bet-buttons button:hover {
  border: 0;
}
.main-mv-no-pinned-runners-line-wrapper {
  margin: 0 9px 0 8px;
  border-top: 1px solid #dfdfdf;
  border-bottom: 1px solid #dfdfdf;
}
.main-mv-no-pinned-runners-line {
  width: calc(100% + 1px);
}
.main-mv-no-pinned-runners-line .no-pinned-runners-label {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  padding-left: 10px;
  line-height: 29px;
}
.main-mv-no-pinned-runners-line .bet-button {
  box-sizing: content-box;
  width: 8%;
  border-left: 1px solid #f4f4f4;
}
.main-mv-no-pinned-runners-line .right-column {
  border-right: 1px solid #f4f4f4;
  border-left-width: 0;
}
.main-mv-no-pinned-runners-line .back-button {
  border-left: 1px solid #fff;
  background-color: #e0f1ff;
}
.main-mv-no-pinned-runners-line .lay-button {
  border-left: 1px solid #fff;
  background-color: #fdecf0;
}
.main-mv-no-pinned-runners-line .bsp-button {
  box-sizing: content-box;
  width: 5%;
}
.main-mv-no-pinned-runners-line .bsp-near-far {
  box-sizing: content-box;
  width: 8%;
}
@media only screen and (max-width: 1279px) {
  .main-mv-no-pinned-runners-line .no-pinned-runners-label {
    max-width: 235px;
  }
}
.main-mv-container {
  padding-bottom: 14px;
}
.main-mv-runners-list-wrapper {
  position: relative;
}
.mv-sticky-header {
  background-color: #fff;
  border-bottom: 1px solid #fff;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  z-index: 11;
}
.is-scrolling .mv-sticky-header {
  box-shadow: rgba(0, 0, 0, 0.3) 0 2px 2px 0;
}
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .page-content .is-scrolling {
    border-top: 1px solid rgba(0, 0, 0, 0.3);
  }
  .mv-sticky-header {
    margin-right: 17px;
  }
}
@supports (-ms-ime-align: auto) {
  .page-content .is-scrolling {
    border-top: 1px solid rgba(0, 0, 0, 0.3);
  }
  .mv-sticky-header {
    margin-right: 12px;
  }
}
.market-rotator {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: row;
  flex-direction: row;
  height: 24px;
}
.market-rotator .rotator-transparency-container {
  overflow: hidden;
  -ms-flex-positive: 1;
  flex-grow: 1;
  -ms-flex-negative: 1;
  flex-shrink: 1;
}
.market-rotator .rotator-values-container {
  position: relative;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: row;
  flex-direction: row;
  -ms-flex-align: center;
  align-items: center;
  text-align: center;
  transition: 0.5s cubic-bezier(0.23, 1, 0.33, 1);
}
.market-rotator .rotator-value {
  color: #7f7f7f;
}
.market-rotator .rotator-value.is-selected-value {
  color: #1e1e1e;
  font-weight: 700;
  cursor: pointer;
}
.market-rotator .rotator-value.is-selected-value:hover {
  background-color: #ebebeb;
}
.market-rotator .rotator-value.is-highlighted-value {
  color: #00f;
}
.market-rotator .rotator-values-container .rotator-value {
  -ms-flex: 1 0 33.3333%;
  flex: 1 0 33.3333%;
  font-size: 11px;
  line-height: 24px;
}
.market-rotator .rotator-left {
  margin-right: 15px;
}
.market-rotator .rotator-right {
  margin-left: 15px;
}
.market-rotator .rotator-left,
.market-rotator .rotator-right {
  -ms-flex-positive: 0;
  flex-grow: 0;
  -ms-flex-negative: 0;
  flex-shrink: 0;
  border: 0;
  padding: 7px;
  background-color: transparent;
}
.market-rotator .rotator-left:focus,
.market-rotator .rotator-right:focus {
  outline: 0;
}
.market-rotator .rotator-left-icon,
.market-rotator .rotator-right-icon {
  fill: #303030;
  width: 11px;
}
.market-rotator .rotator-right-icon {
  transform: rotate(180deg);
}
.market-rotator .rotator-left:hover .rotator-left-icon,
.market-rotator .rotator-right:hover .rotator-right-icon {
  fill: #7f7f7f;
}
.market-rotator .rotator-left:disabled .rotator-left-icon,
.market-rotator .rotator-right:disabled .rotator-right-icon {
  fill: #dfdfdf;
}
.ie10 .market-rotator {
  display: -ms-flexbox;
  -ms-flex-direction: row;
}
.ie10 .market-rotator .rotator-transparency-container {
  -ms-flex-positive: 1;
  -ms-flex-negative: 1;
}
.ie10 .market-rotator .rotator-values-container {
  display: -ms-flexbox;
  -ms-flex-direction: row;
  -ms-flex-align: center;
}
.ie10 .market-rotator .rotator-values-container .rotator-value {
  -ms-flex-positive: 1;
  -ms-flex-negative: 0;
  -ms-flex-preferred-size: 33.3333%;
}
.marketview-header-wrapper-container {
  clear: both;
}
.marketview-header-wrapper-container .star-favourites {
  float: left;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container {
  padding: 8px 8px 12px;
  margin: 0;
  cursor: default;
  overflow: auto;
  clear: both;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.new-theme {
  padding-left: 0;
  padding-right: 0;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.closed {
  padding: 5px 8px 7px;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container
  .market-type {
  color: #1e1e1e;
  border-bottom: 1px solid #dfdfdf;
  padding-bottom: 4px;
  margin-bottom: 8px;
  font-weight: 700;
  font-size: 12px;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.has-favourites {
  position: relative;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.has-favourites
  .star-favourites-container {
  position: absolute;
  top: 10px;
  left: 8px;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.has-favourites.closed
  .star-favourites-container {
  top: 7px;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.has-favourites.new-theme
  .star-favourites-container {
  top: 15px;
  left: 14px;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.has-favourites.new-theme.closed
  .star-favourites-container {
  top: 12px;
}
.marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.has-favourites
  .mv-header-main-section
  > :first-child {
  margin-left: 22px;
}
.marketview-header-wrapper-container .market-going-inplay .market-status-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1202px;
}
.marketview-header-wrapper-container .market-inplay .market-status-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1186px;
}
.marketview-header-wrapper-container .cashout-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1032px;
}
.marketview-header-wrapper-container .market-rules-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2455px;
  border-radius: 2px 0 0 2px;
}
.marketview-header-wrapper-container .ah-pnl-table-wrapper {
  position: static;
  margin-right: 8px;
}
.marketview-header-wrapper-container .ah-pnl-table {
  padding-bottom: 0;
}
.marketview-header-wrapper-container
  .mv-header-container
  .pin-runners
  .pin-runners-icon {
  width: 10px;
  margin-left: 7px;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2031px;
}
.marketview-list-runners-component {
  margin-bottom: 0;
  position: relative;
}
.marketview-list-runners-component .loading-market {
  display: none;
}
.marketview-list-runners-component .pnl {
  float: left;
  margin-left: 5px;
  padding-bottom: 2px;
}
.marketview-list-runners-component .pnl.below-runner-info {
  clear: both;
}
.marketview-list-runners-component .greyhound-racing .runner-silk {
  padding-left: 2px;
}
.marketview-list-runners-component
  .horse-racing
  .runner-silk
  .saddle-cloth-alpha {
  margin-left: 3px;
}
.marketview-list-runners-component .mv-runner-list-container {
  padding: 0 8px;
}
.marketview-list-runners-component .runner-list-wrapper {
  overflow-x: auto;
  overflow-y: hidden;
}
.marketview-list-runners-component .market-graph-container {
  float: left;
  overflow: hidden;
  width: 13px;
  height: 29px;
  padding-left: 2px;
}
.marketview-list-runners-component .market-graph-container .market-graph {
  margin-top: 7px;
  height: 17px;
  width: 100%;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -193px;
}
.marketview-list-runners-component .market-graph-container .market-graph:hover {
  transform: scale(1.1);
}
.marketview-list-runners-component .new-runner-info.with-runner-timeform-info {
  position: relative;
}
.marketview-list-runners-component
  .new-runner-info.with-runner-timeform-info:hover {
  background-color: #f6f6f6;
}
.marketview-list-runners-component
  .new-runner-info.with-runner-timeform-info
  .runner-info {
  cursor: pointer;
}
.marketview-list-runners-component
  .new-runner-info.with-runner-timeform-info
  .market-graph,
.marketview-list-runners-component
  .new-runner-info.with-runner-timeform-info
  .runner-numbers,
.marketview-list-runners-component
  .new-runner-info.with-runner-timeform-info
  .runner-silk {
  position: relative;
}
.marketview-list-runners-component .new-runner-info.with-pin-runners {
  padding-left: 12px;
}
.marketview-list-runners-component .runner-timeform-info-icon {
  float: left;
  width: 20px;
  height: 20px;
}
.marketview-list-runners-component .runner-timeform-info-icon--clickable {
  cursor: pointer;
}
.marketview-list-runners-component .runner-timeform-info-dropdown-icon,
.marketview-list-runners-component
  .runner-timeform-info-dropdown-icon.expanded {
  transition: transform 0.2s ease;
  -moz-transition: transform 0.2s ease;
  -webkit-transition: transform 0.2s ease;
}
.marketview-list-runners-component .runner-timeform-info-dropdown-icon {
  color: #000;
  fill: #000;
  float: right;
  margin-top: 12px;
  margin-right: 10px;
  transform: rotate(-90deg);
  -ms-transform: rotate(-90deg);
}
.marketview-list-runners-component
  .runner-timeform-info-dropdown-icon.expanded {
  transform: rotate(90deg);
  -ms-transform: rotate(90deg);
}
.marketview-list-runners-component
  .runner-past-races__column--av-content:hover {
  background-color: #f6f6f6;
}
.marketview-list-runners-component .runner-data-container .greyhound-silk-1 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1244px;
}
.marketview-list-runners-component .runner-data-container .greyhound-silk-2 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1262px;
}
.marketview-list-runners-component .runner-data-container .greyhound-silk-3 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1280px;
}
.marketview-list-runners-component .runner-data-container .greyhound-silk-4 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1298px;
}
.marketview-list-runners-component .runner-data-container .greyhound-silk-5 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1316px;
}
.marketview-list-runners-component .runner-data-container .greyhound-silk-6 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1334px;
}
.marketview-list-runners-component .runner-data-container .greyhound-silk-7 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1352px;
}
.marketview-list-runners-component .runner-data-container .greyhound-silk-8 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1370px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-1 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 0;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-1A {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -20px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-1B {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -40px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-1C {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -60px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-1D {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -80px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-1X {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -100px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-1Y {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -120px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-2 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -140px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-2B {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -160px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-2C {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -180px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-2X {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -200px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-3 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -220px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-3C {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -240px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-3D {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -260px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-3E {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -280px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-3X {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -300px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-4 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -320px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-4D {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -340px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-4X {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -360px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-5 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -380px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-6 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -400px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-7 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -420px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-8 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -440px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-9 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -460px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-10 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -480px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-11 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -500px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-11F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -520px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-12 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -540px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-12F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -560px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-13 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -580px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-13F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -600px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-14 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -620px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-14F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -640px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-15 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -660px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-15F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -680px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-16 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -700px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-16F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -720px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-17 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -740px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-17F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -760px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-18 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -780px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-18F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -800px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-19 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -820px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-19F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -840px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-20 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -860px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-20F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -880px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-21 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -900px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-21F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -920px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-22 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -940px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-22F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -960px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-23 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -980px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-23F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1000px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-24 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1020px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-24F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1040px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-25 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1060px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-25F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1080px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-26 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1100px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-26F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1120px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-27 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1140px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-27F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1160px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-28 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1180px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-28F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1200px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-29 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1220px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-29F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1240px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-30 {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1260px;
}
.marketview-list-runners-component .runner-data-container .saddle-cloth-30F {
  background: transparent
    url(images/app/common/assets/images/saddlecloths-sprite_4627_.gif) no-repeat
    0 -1280px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-1 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2049px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-2 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2067px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-3 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2085px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-4 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2103px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-5 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2121px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-6 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2139px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-7 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2157px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-8 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2175px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-9 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2193px;
}
.marketview-list-runners-component
  .aus-greyhounds
  .runner-data-container
  .greyhound-silk-10 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2211px;
}
.marketview-list-runners-component .runner-status {
  min-height: 31px;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 11px;
  text-align: left;
  color: #233a47;
  float: left;
}
.marketview-list-runners-component .runner-status .non-runner-container {
  line-height: 30px;
  padding-top: 10px;
}
.marketview-list-runners-component
  .runner-status
  .non-runner-container
  .non-runner-adjustment-factor {
  float: left;
  line-height: 30px;
}
.marketview-list-runners-component .runner-status .runner-winner-label {
  font-weight: 700;
  display: block;
  padding-top: 2px;
}
.marketview-list-runners-component .runner-status .runner-winner-without-bsp {
  padding-top: 8px;
}
.marketview-list-runners-component .mv-runner-list {
  min-height: 1px;
  height: 100%;
  width: 100%;
  border: 0;
  border-spacing: 0;
  padding: 0;
}
.marketview-list-runners-component .bet-buttons .back,
.marketview-list-runners-component .bet-buttons .lay {
  background-color: #fff;
}
.marketview-list-runners-component .bet-buttons .back-selection-button.changed,
.marketview-list-runners-component .bet-buttons .back.changed,
.marketview-list-runners-component .bet-buttons .lay-selection-button.changed,
.marketview-list-runners-component .bet-buttons .lay.changed,
.marketview-list-runners-component .bsp-button .back.changed,
.marketview-list-runners-component .bsp-button .lay.changed,
.marketview-list-runners-component
  .runner-item
  .btn.back-selection-button.changed,
.marketview-list-runners-component .runner-item .btn.changed,
.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-off:nth-child(1).changed,
.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-on:nth-child(3).changed {
  animation-duration: 0.3s;
  -moz-animation-duration: 0.3s;
  -webkit-animation-duration: 0.3s;
}
.marketview-list-runners-component .bet-buttons .back.changed,
.marketview-list-runners-component .bet-buttons .lay.changed {
  animation-name: newHighlightGrey;
}
.marketview-list-runners-component .bet-buttons .back-selection-button,
.marketview-list-runners-component .bsp-button .back {
  background-color: #a6d8ff;
}
.marketview-list-runners-component .bet-buttons .back-selection-button.selected,
.marketview-list-runners-component .bet-buttons .lay-selection-button.selected,
.marketview-list-runners-component .bsp-button .back.selected,
.marketview-list-runners-component .bsp-button .lay.selected {
  box-shadow: inset 0 0 8px 0.2px rgba(127, 127, 127, 0.6);
}
.marketview-list-runners-component .bet-buttons .back-selection-button.selected,
.marketview-list-runners-component .bsp-button .back.selected {
  background-color: #75c2fd;
}
.marketview-list-runners-component .bet-buttons .back-selection-button.changed,
.marketview-list-runners-component .bsp-button .back.changed {
  animation-name: newHighlightBack;
}
.marketview-list-runners-component .bet-buttons .lay-selection-button,
.marketview-list-runners-component .bsp-button .lay {
  background-color: #fac9d4;
}
.marketview-list-runners-component .bet-buttons .lay-selection-button.selected,
.marketview-list-runners-component .bsp-button .lay.selected {
  background-color: #f694aa;
}
.marketview-list-runners-component .bet-buttons .lay-selection-button.changed,
.marketview-list-runners-component .bsp-button .lay.changed {
  animation-name: newHighlightLay;
}
.marketview-list-runners-component .runner-line {
  height: 100%;
  border-bottom: 1px solid #dfdfdf;
}
.marketview-list-runners-component .runner-item .sp-odds .sp-near-far,
.marketview-list-runners-component .runner-line .back,
.marketview-list-runners-component .runner-line .lay {
  border: 0;
  margin: 0;
  padding: 0;
}
.marketview-list-runners-component .runner-line .back,
.marketview-list-runners-component .runner-line .lay {
  width: 100%;
  height: 100%;
}
.marketview-list-runners-component .runner-line .back {
  border-left: 1px solid #dfdfdf;
}
.marketview-list-runners-component .runner-line .back.back-selection-button {
  border-right: 1px solid #fff;
  border-left: 0;
}
.marketview-list-runners-component .runner-line .lay {
  border-right: 1px solid #dfdfdf;
}
.marketview-list-runners-component .runner-line .lay.lay-selection-button {
  border-right: 0;
}
.marketview-list-runners-component .runner-line .price {
  font-weight: 700;
  display: block;
}
.marketview-list-runners-component .runner-line .size {
  display: block;
}
.marketview-list-runners-component
  .runner-line
  .runner-data-container.with-pnl.without-race-card-info {
  height: 15px;
}
.marketview-list-runners-component
  .mv-runner-list
  .runner-line
  .runner-data-container.with-pnl.without-race-card-info
  .runner-name {
  line-height: 12px;
}
.marketview-list-runners-component .runner-line .name-saddlecloth .name {
  max-width: calc(100% - 63px);
}
.marketview-list-runners-component .runner-line .name-silk .name {
  max-width: calc(100% - 86px);
}
.marketview-list-runners-component .runner-line .bet-buttons {
  width: 8%;
  text-align: center;
  overflow: hidden;
}
.marketview-list-runners-component .runner-line .back-cell,
.marketview-list-runners-component .runner-line .bsp-near-far,
.marketview-list-runners-component .runner-line .lay-cell {
  line-height: 0;
  height: 100%;
}
.marketview-list-runners-component .runner-line .back-cell.bsp-button,
.marketview-list-runners-component .runner-line .back-cell.first-lay-cell,
.marketview-list-runners-component .runner-line .back-cell.last-back-cell,
.marketview-list-runners-component .runner-line .bsp-near-far.bsp-button,
.marketview-list-runners-component .runner-line .bsp-near-far.first-lay-cell,
.marketview-list-runners-component .runner-line .bsp-near-far.last-back-cell,
.marketview-list-runners-component .runner-line .lay-cell.bsp-button,
.marketview-list-runners-component .runner-line .lay-cell.first-lay-cell,
.marketview-list-runners-component .runner-line .lay-cell.last-back-cell {
  border-bottom: 1px solid #fff;
}
.marketview-list-runners-component .runner-line .bsp-button {
  width: 5%;
}
.marketview-list-runners-component .runner-line .bsp-button .back {
  border-right: 0;
  border-left: 0;
}
.marketview-list-runners-component .runner-line .bsp-button .lay {
  border-left: 0;
  border-right: 1px solid #fff;
}
.marketview-list-runners-component .runner-line .bsp-near-far {
  width: 8%;
  text-align: center;
}
.marketview-list-runners-component .runner-line .runner-metadata-list {
  z-index: 51;
}
.marketview-list-runners-component .runner-line:first-child .back-cell,
.marketview-list-runners-component .runner-line:first-child .bsp-near-far,
.marketview-list-runners-component .runner-line:first-child .lay-cell,
.marketview-list-runners-component .runner-line:first-child .new-runner-info {
  border-top: 1px solid #dfdfdf;
}
.marketview-list-runners-component
  .runner-line:last-child
  .back-cell.bsp-button,
.marketview-list-runners-component
  .runner-line:last-child
  .back-cell.last-back-cell,
.marketview-list-runners-component .runner-line:last-child .lay-cell.bsp-button,
.marketview-list-runners-component
  .runner-line:last-child
  .lay-cell.first-lay-cell {
  overflow: hidden;
  border-bottom: 1px solid #dfdfdf;
}
.marketview-list-runners-component .runner-line:last-child .back,
.marketview-list-runners-component .runner-line:last-child .lay {
  margin-bottom: 2px;
}
.marketview-list-runners-component .bet-buttons .back:hover,
.marketview-list-runners-component .bet-buttons .lay:hover {
  background-color: #dfdfdf;
}
.marketview-list-runners-component .bet-buttons .back-selection-button:hover,
.marketview-list-runners-component .bsp-button .back:hover {
  background-color: #75c2fd;
}
.marketview-list-runners-component .bet-buttons .lay-selection-button:hover,
.marketview-list-runners-component .bsp-button .lay:hover {
  background-color: #f694aa;
}
.marketview-list-runners-component .mv-runner-list.fixed-size .bet-buttons {
  min-width: 60px;
}
.marketview-list-runners-component
  .mv-runner-list.small
  .runner-line
  .bsp-button
  .back {
  border-right: 1px solid #fff;
}
.marketview-list-runners-component .market-graph-container .market-graph:active,
.marketview-list-runners-component .market-graph-container .market-graph:hover {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -208px;
}
.marketview-list-runners-component .runner-removed-winner-looser {
  float: right;
  width: 48%;
  text-align: left;
  color: #233a47;
  vertical-align: middle;
}
.marketview-list-runners-component
  .runner-removed-winner-looser
  .non-runner-label {
  font-weight: 700;
  font-size: 12px;
  margin-right: 5px;
  float: left;
  padding-right: 5px;
  line-height: 30px;
}
.marketview-list-runners-component
  .runner-removed-winner-looser
  .runner-winner {
  vertical-align: middle;
  display: inline;
}
.marketview-list-runners-component
  .mv-runner-list
  .runner-removed-winner-looser
  .runner-winner
  .runner-winner-without-bsp {
  line-height: 30px;
  padding-top: 0;
}
.marketview-list-runners-component
  .runner-removed-winner-looser
  .runner-winner-label {
  padding-top: 4px;
  font-weight: 700;
}
.marketview-list-runners-component
  .mv-runner-list.large
  .runner-line
  .runner-removed-winner-looser {
  width: 65%;
}
.marketview-list-runners-component .sp-bets-container {
  float: right;
}
.marketview-list-runners-component .sp-odds-section {
  float: left;
}
.marketview-list-runners-component .runner-item {
  margin: 0;
  border-bottom: 1px solid #dfdfdf;
}
.marketview-list-runners-component .runner-item:first-child {
  margin-top: 1px;
  border-top: 1px solid #dfdfdf;
}
.marketview-list-runners-component .runner-item .btn {
  border-left: 1px solid #fff;
  border-bottom: 1px solid #fff;
  height: 30px;
  line-height: 12px;
}
.marketview-list-runners-component
  .runner-item
  .btn.back.back-selection-button {
  border-right: 0;
}
.marketview-list-runners-component .runner-item .btn:focus {
  outline: 0;
}
.marketview-list-runners-component .runner-item .btn .price {
  font-weight: 700;
  display: block;
}
.marketview-list-runners-component .runner-item .btn-all {
  font-size: 11px;
}
.marketview-list-runners-component .runner-item .sp-odds {
  background-color: #fff;
  overflow: hidden;
  padding: 0;
}
.marketview-list-runners-component .runner-item .sp-odds .sp-near-far {
  line-height: 12px;
  height: 0;
}
.marketview-list-runners-component .runner-item .sp-odds .sp-near {
  margin-top: 4px;
}
.marketview-list-runners-component .runner-item.haspnl .btn {
  height: 45px;
}
.marketview-list-runners-component .runner-item.haspnl .sp-odds {
  margin-top: 8px;
}
.marketview-list-runners-component
  .runner-item.haspnl
  .back.back-selection-button,
.marketview-list-runners-component .runner-item.haspnl .btn.back,
.marketview-list-runners-component .runner-item.haspnl .btn.lay,
.marketview-list-runners-component
  .runner-item.haspnl
  .lay.market-depth-off:nth-child(1),
.marketview-list-runners-component
  .runner-item.haspnl
  .lay.market-depth-on:nth-child(3) {
  height: 45px;
}
.marketview-list-runners-component .runner-item .back-bets .btn:first-child {
  margin-left: 0;
}
.marketview-list-runners-component .runner-item .btn.selected {
  outline: 0;
}
.marketview-list-runners-component .runner-item.middle .runner-data-container {
  line-height: 26px;
}
.marketview-list-runners-component
  .runner-item
  .runner-data-container
  .runner-info
  .name {
  float: none;
}
.marketview-list-runners-component
  .runner-item.has-sp-bets.only-back-without-market-depth
  .runner-status,
.marketview-list-runners-component
  .runner-item.has-sp-bets.without-market-depth
  .runner-status,
.marketview-list-runners-component
  .runner-item.only-back-without-market-depth
  .runner-status,
.marketview-list-runners-component
  .runner-item.without-market-depth
  .runner-status {
  text-align: right;
}
.marketview-list-runners-component
  .runner-item.has-sp-bets
  .btn.lay.market-depth-off:nth-child(1).depth-lay-2,
.marketview-list-runners-component
  .runner-item.has-sp-bets
  .btn.lay.market-depth-on:nth-child(3).depth-lay-2 {
  border-left: 1px solid #fff;
}
.marketview-list-runners-component .runner-item .sp-projected-odds {
  font-size: 11px;
}
.marketview-list-runners-component .runner-item.has-sp-near-far-bets .sp-odds {
  padding: 0;
  border-bottom: 0;
}
.marketview-list-runners-component
  .runner-item.has-sp-near-far-bets
  .sp-near-far-container,
.marketview-list-runners-component
  .runner-item.has-sp-near-far-bets
  .sp-projected-odds {
  line-height: 29px;
  text-align: center;
}
.marketview-list-runners-component
  .runner-item.has-sp-near-far-bets.only-back-without-market-depth
  .runner-status {
  text-align: right;
}
.marketview-list-runners-component
  .runner-item.has-sp-reconciled
  .sp-actual-starting-price {
  text-align: center;
  border-bottom: 0;
  line-height: 25px;
}
.marketview-list-runners-component
  .runner-item.has-sp-reconciled.only-back-without-market-depth
  .runner-status {
  text-align: right;
}
.marketview-list-runners-component
  .runner-item.has-sp-reconciled.without-market-depth
  .sp-odds {
  padding: 0;
}
.marketview-list-runners-component .runner-item .btn.changed {
  animation-name: highlightGrey;
}
.marketview-list-runners-component
  .runner-item
  .btn.back-selection-button.changed {
  animation-name: highlightBack;
}
.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-off:nth-child(1).changed,
.marketview-list-runners-component
  .runner-item
  .btn.lay.market-depth-on:nth-child(3).changed {
  animation-name: highlightLay;
}
.marketview-list-runners-component .removed-runner-info {
  float: left;
}
.marketview-list-runners-component .runner-inner-container-header-overlay,
.marketview-list-runners-component .runner-list-overlay {
  background: #fff;
}
@media screen and (max-width: 80em) {
  .marketview-list-runners-component .btn .size,
  .marketview-list-runners-component .btn.sp-btn-near-far.sp-back,
  .marketview-list-runners-component .btn.sp-btn-near-far.sp-lay,
  .marketview-list-runners-component .mv-bet-button .bet-button-size,
  .marketview-list-runners-component .size,
  .marketview-list-runners-component .sp-far,
  .marketview-list-runners-component .sp-near {
    font-size: 10px;
  }
}
@media screen and (min-width: 80em) {
  .marketview-list-runners-component .btn .size,
  .marketview-list-runners-component .btn.sp-btn-near-far.sp-back,
  .marketview-list-runners-component .btn.sp-btn-near-far.sp-lay,
  .marketview-list-runners-component .mv-bet-button .bet-button-size,
  .marketview-list-runners-component .size,
  .marketview-list-runners-component .sp-far,
  .marketview-list-runners-component .sp-near {
    font-size: 11px;
  }
}
.marketview-container.greyhound-racing
  .marketview-list-runners-component
  .runner-item {
  position: relative;
}
.marketview-container.greyhound-racing
  .marketview-list-runners-component
  .non-runner-container {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  width: 100%;
  height: 100%;
  padding: 0;
}
.marketview-container.greyhound-racing
  .marketview-list-runners-component
  .non-runner-label.vacant {
  float: none;
  text-align: center;
  margin: auto;
  display: block;
}
.marketview-container .loading-wrapper {
  margin-top: 70px;
}
.marketview-container .market-rules-modal-dialog {
  color: #444;
}
.marketview-container .market-rules-modal-dialog .dialog {
  width: 500px;
  line-height: 1.4;
}
.marketview-container .market-rules-modal-dialog a,
.marketview-container .market-rules-modal-dialog a:active,
.marketview-container .market-rules-modal-dialog a:hover,
.marketview-container .market-rules-modal-dialog a:visited {
  color: #2489d5;
}
.marketview-container .market-rules-modal-dialog .market-rules-name {
  padding: 0 16px 10px 0;
  border-bottom: 2px solid #273a47;
  font-size: 18px;
  text-decoration: none;
  margin: 0 0 6px;
}
.marketview-container .market-rules-modal-dialog .market-rules-commission-title,
.marketview-container .market-rules-modal-dialog .market-rules-description,
.marketview-container
  .market-rules-modal-dialog
  .market-rules-event-start-time-title,
.marketview-container .market-rules-modal-dialog .market-rules-name {
  font-weight: 700;
}
.marketview-container .market-rules-modal-dialog .market-rules-description {
  margin: 4px 0;
}
.marketview-container .market-rules-modal-dialog .market-rules-clarifications {
  padding: 10px 0;
}
.marketview-container .market-rules-modal-dialog .market-rules-licence {
  padding-bottom: 20px;
}
@media only screen and (max-width: 1024px) {
  .market-going-inplay {
    max-width: 90px;
  }
}
@media only screen and (max-width: 1024px),
  only screen and (max-width: 1279px) {
  .bf-market-view-scroll .market-info-container {
    width: 100%;
    float: left;
    padding-bottom: 5px;
  }
}
@media only screen and (max-width: 1600px) {
  .bf-market-view-scroll
    .marketview-list-runners-component
    .runner-item.to-be-place-pnl.haspnl
    .btn,
  .bf-market-view-scroll
    .marketview-list-runners-component
    .runner-item.to-be-place-pnl.haspnl
    .btn.back,
  .bf-market-view-scroll
    .marketview-list-runners-component
    .runner-item.to-be-place-pnl.haspnl
    .btn.lay {
    height: 42px;
  }
}
.marketview-list-runners-component
  .runner-line.loser-runner
  .runner-data-container,
.marketview-list-runners-component
  .runner-line.removed-runner
  .runner-data-container,
.marketview-list-runners-component
  .runner-line.winner-runner
  .runner-data-container {
  float: none;
}
.marketview-list-runners-component.market-closed
  .loser-runner
  .runner-info-container
  .runner-data-container,
.marketview-list-runners-component.market-closed
  .loser-runner
  .runner-info-left-elems-container,
.marketview-list-runners-component.market-closed
  .loser-runner
  .runner-removed-winner-looser
  .non-runner-container,
.marketview-list-runners-component.market-closed
  .removed-runner
  .runner-info-container
  .runner-data-container,
.marketview-list-runners-component.market-closed
  .removed-runner
  .runner-info-left-elems-container,
.marketview-list-runners-component.market-closed
  .removed-runner
  .runner-removed-winner-looser
  .non-runner-container {
  -moz-opacity: 0.13;
  -khtml-opacity: 0.13;
  -webkit-opacity: 0.13;
  opacity: 0.13;
}
.marketview-list-runners-component
  .runner-line.removed-runner.removed-runner
  .non-runner-container {
  position: static;
}
.marketview-list-runners-component
  .mv-runner-list
  .runner-line.removed-runner.removed-runner
  .non-runner-container
  .non-runner-label.vacant {
  text-align: left;
}
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .runner-timeform-info-container td {
    max-width: 1px;
  }
}
@media only screen and (max-width: 1279px) {
  .market-going-inplay {
    max-width: 123px;
  }
  .marketview-list-runners-component
    .marketview-list-runners-component
    .runner-item.each-way-multi-pnl-runner.haspnl
    .btn.back,
  .marketview-list-runners-component
    .marketview-list-runners-component
    .runner-item.each-way-multi-pnl-runner.haspnl
    .btn.lay {
    height: 54px;
  }
  .marketview-list-runners-component
    .runner-removed-winner-looser
    .non-runner-label {
    line-height: 15px;
    display: block;
  }
  .marketview-list-runners-component
    .runner-removed-winner-looser
    .non-runner-adjustment-factor {
    line-height: 15px;
  }
}
.pin {
  border: 0;
  padding: 0;
}
.pin.pin-runner {
  background-color: #c2c2c2;
}
.pin.pin-runner:disabled {
  background-color: #e7e7e7;
}
.pin .svg-icon-default {
  margin-top: 1px;
}
.pin.unpin-runner {
  background-color: #f33e3e;
}
.pin.unpin-runner .svg-icon-default {
  width: 11px;
  height: 12px;
}
.pin:disabled > .svg-icon-default {
  pointer-events: none;
}
.marketview-list-runners-component .mv-runner-list .runner-pin-placeholder {
  width: 32px;
  overflow: hidden;
  border-top: 1px solid #dfdfdf;
}
.marketview-list-runners-component
  .mv-runner-list
  .runner-pin-placeholder
  .pin {
  outline: 0;
  width: 32px;
  margin: -100px 0;
  padding: 100px 0;
}
.marketview-list-runners-component
  .mv-runner-list
  .runner-line:last-child
  .back,
.marketview-list-runners-component
  .mv-runner-list
  .runner-line:last-child
  .lay {
  margin-bottom: 0;
}
.main-mv-pin-header {
  background-color: #ebebeb;
  color: #1e1e1e;
  width: calc(100% - 16px);
  margin-left: 8px;
}
.main-mv-pin-header.main-mv-pin-header-my-pins {
  border-top: 1px solid #dfdfdf;
}
.main-mv-pin-header .main-mv-pin-header-market-label,
.main-mv-pin-header .main-mv-pin-header-my-pins-label {
  line-height: 16px;
  height: 16px;
  padding-left: 10px;
}
.runners-list-pinned > .marketview-list-runners-component {
  margin-bottom: 0;
}
.mini-mv-header {
  background-color: #424242;
  border-radius: 2px;
  color: #fff;
  font-size: 12px;
  height: 28px;
  padding: 10px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  -ms-flex-pack: center;
  justify-content: center;
}
.mini-mv-header__event-name {
  font-weight: 700;
  line-height: 14px;
}
.mini-mv {
  margin-bottom: 8px;
}
.mini-mv .runners-header {
  margin: 6px 0 5px;
  width: 100%;
}
.mini-mv .rh-runner-name-header {
  width: 66%;
  line-height: 1;
}
.mini-mv .rh-line.without-lay .rh-runner-name-header {
  width: 82%;
}
.mini-mv .rh-matched-amount-label {
  color: #7f7f7f;
}
.mini-mv
  .marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container {
  padding-bottom: 0;
}
.mini-mv
  .marketview-header-wrapper-container
  .marketview-header-wrapper-bottom-container.closed {
  padding: 8px 0 0;
}
.mini-mv .rh-label-all.is-small {
  width: 15%;
}
.mini-mv .rh-label-all.is-small .rh-label-back,
.mini-mv .rh-label-all.is-small .rh-label-lay {
  width: 100%;
  padding: 0;
}
.mini-mv td.new-runner-info .rh-label-all {
  width: 11%;
}
.mini-mv td.new-runner-info {
  width: 70%;
  padding-left: 8px;
}
.mini-mv td.new-runner-info.without-lay {
  width: 83%;
}
.mini-mv .rh-line.without-lay .rh-label-all {
  width: 18%;
}
.mini-mv .expand-collapse-link,
.mini-mv .mini-mv-full-market-link {
  margin-top: 7px;
  color: #1e1e1e;
  font-size: 12px;
  text-align: right;
  text-decoration: none;
  cursor: pointer;
  display: block;
}
.mini-mv .expand-collapse-link {
  border-bottom: 1px solid #dfdfdf;
}
.mini-mv .expand-collapse-link:hover,
.mini-mv .mini-mv-full-market-link:hover {
  text-decoration: underline;
}
.mini-mv .expand-collapse-link .arrow,
.mini-mv .mini-mv-full-market-link .arrow {
  fill: #7f7f7f;
  width: 8px;
  height: 9px;
  margin-left: 4px;
}
.mini-mv .mini-mv-full-market-link .arrow {
  transform: rotate(180deg);
  -ms-transform: rotate(180deg);
}
.mini-mv .expand-collapse-link .arrow {
  transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transition: all 0.2s ease;
  -moz-transition: all 0.2s ease;
  -webkit-transition: all 0.2s ease;
}
.mini-mv .expand-collapse-link.collapsed .arrow {
  transform: rotate(270deg);
  -ms-transform: rotate(270deg);
}
.mini-mv .suspended-overlay-container {
  margin-top: -23px;
  top: 50%;
}
.mini-mv .marketview-list-runners-component {
  margin-bottom: 0;
}
.mini-mv .marketview-list-runners-component .mv-runner-list-container {
  padding: 0;
}
.mini-mv .marketview-list-runners-component .mv-runner-list {
  table-layout: fixed;
}
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line
  .bet-buttons {
  min-width: 0;
  width: 16%;
}
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line
  .bet-buttons.without-lay {
  width: 18%;
}
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line
  .bet-buttons.without-lay
  .back-button {
  border-right: 0;
}
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line
  .name-silk
  .name {
  max-width: 80%;
}
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line.winner-runner
  .name-silk
  .name {
  max-width: 46%;
}
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line
  button.back,
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line
  button.lay {
  padding-bottom: 1px;
}
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line:last-child
  .back,
.mini-mv
  .marketview-list-runners-component
  .mv-runner-list
  .runner-line:last-child
  .lay {
  margin-bottom: 0;
}
.mini-mv .inline-betting-container.ng-leave {
  transition: all 0.25s linear;
  -moz-transition: all 0.25s linear;
  -webkit-transition: all 0.25s linear;
  opacity: 1;
}
.mini-mv .inline-betting-container.ng-leave.ng-leave-active {
  opacity: 0;
}
.mini-mv .mini-mv-runners-list-wrapper {
  position: relative;
}
.mini-mv .mini-market-rotator {
  max-width: 392px;
  margin-left: auto;
}
.mini-mv .mini-market-rotator + bf-runners-header {
  display: block;
  border-top: 1px solid #dfdfdf;
}
.mini-mv:not(.mini-market-rotator) + bf-runners-header .runners-header {
  margin: 8px 0 6px;
}
@media only screen and (max-width: 1279px) {
  .mini-mv .rh-runner-name-header {
    width: 58%;
  }
  .mini-mv td.new-runner-info {
    width: 60%;
  }
  .mini-mv .rh-label-all.is-small {
    width: 20%;
  }
  .mini-mv .suspended-overlay-container {
    left: -28%;
  }
  .mini-mv
    .marketview-list-runners-component
    .mv-runner-list
    .runner-line
    .bet-buttons {
    width: 21%;
  }
  .mini-mv
    .marketview-list-runners-component
    .mv-runner-list
    .runner-line
    .bet-buttons
    .bet-button-size {
    font-size: 10px;
  }
}
.runners-header {
  margin: 5px 8px 0;
  width: calc(100% - 16px);
}
.rh-line {
  vertical-align: bottom;
}
.rh-runner-name-header {
  line-height: 18px;
}
.rh-selections-count-label {
  padding-right: 15%;
}
.rh-matched-amount-label {
  margin-left: 9px;
}
.rh-each-way-terms {
  font-weight: 700;
}
@media only screen and (max-width: 1279px) {
  .rh-each-way-terms {
    max-width: 250px;
    width: 100%;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
}
.rh-book-percentage {
  width: 8%;
}
.rh-bsp-section {
  width: 18%;
  vertical-align: middle;
  text-align: center;
  font-weight: 700;
  background-color: #e9ebec;
}
.rh-bsp-section.is-minimal {
  width: 5%;
}
.rh-bsp-section.is-small {
  width: 10%;
}
.rh-bsp-section.is-medium {
  width: 13%;
}
.rh-bsp-section.is-reconciled {
  width: 8%;
}
.rh-bsp-section.is-suspended {
  cursor: default;
  opacity: 0.5;
}
.rh-bsp-section-label {
  line-height: 18px;
  border-right: 1px solid #fff;
  display: block;
  margin-bottom: -1px;
}
.rh-select-all-buttons {
  width: 16%;
}
.rh-select-all-buttons.is-small {
  width: 8%;
}
.rh-lay-book-percentage,
.rh-select-back-all-button {
  text-align: right;
}
.rh-back-all,
.rh-lay-all {
  width: 65px;
  padding: 3px 5px;
  height: 18px;
  line-height: 13px;
  font-size: 11px;
  font-weight: 700;
  border: 0;
  cursor: pointer;
}
.rh-back-all.is-suspended,
.rh-lay-all.is-suspended {
  cursor: default;
  opacity: 0.5;
}
.rh-back-all-label,
.rh-lay-all-label {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  display: block;
}
.rh-back-all {
  float: right;
  margin-right: 1px;
  background-color: #a6d8ff;
}
.rh-back-all:hover {
  background-color: #75c2fd;
}
.rh-back-all:focus {
  outline: 0;
}
.rh-lay-all {
  float: left;
  background-color: #fac9d4;
}
.rh-lay-all:hover {
  background-color: #f694aa;
}
.rh-lay-all:focus {
  outline: 0;
}
.rh-label-all {
  width: 16%;
  color: #7f7f7f;
  text-align: center;
}
.rh-label-back,
.rh-label-lay {
  color: #7f7f7f;
  width: calc(50% - 10px);
  padding: 3px 5px;
  text-align: center;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.rh-label-back {
  float: right;
  margin-right: 1px;
}
.rh-label-lay {
  float: left;
}
.rh-label-all.is-small {
  width: 8%;
}
.rh-label-all.is-small .rh-label-back,
.rh-label-all.is-small .rh-label-lay {
  width: calc(100% - 10px);
  min-width: 50px;
}
bf-next-race-card {
  display: block;
  -ms-flex: 1 1 100%;
  flex: 1 1 100%;
  margin-right: 1px;
  background-color: #fff;
}
bf-next-race-card:last-child {
  margin-right: 0;
}
.next-race-card {
  height: 58px;
  padding: 0 6px 0 8px;
}
.next-race-card__link {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  height: 100%;
  text-decoration: none;
}
.next-race-card__country {
  display: block;
  -ms-flex: 0 0 20px;
  flex: 0 0 20px;
  height: 12px;
  margin-right: 8px;
}
.next-race-card__info {
  -ms-flex: 1 1 100%;
  flex: 1 1 100%;
}
.next-race-card__status-container {
  -ms-flex: 0 1 0;
  flex: 0 1 0;
  text-align: right;
}
.next-race-card__time,
.next-race-card__venue {
  font-size: 12px;
  font-weight: 700;
  color: #303030;
  display: inline;
}
.next-race-card__info-bottom {
  white-space: nowrap;
  margin-top: 2px;
}
.next-race-card__matched-amount {
  font-size: 11px;
  color: #7f7f7f;
  display: inline-block;
  margin-right: 4px;
}
.next-race-card__live-video,
.next-race-card__on-tv {
  display: inline-block;
  height: 8px;
  margin-right: 4px;
}
.next-race-card__on-tv {
  width: 10px;
}
.next-race-card__on-tv .next-race-card__on-tv-icon {
  margin-bottom: -1px;
  fill: #7f7f7f;
}
.next-race-card__live-video {
  width: 11px;
}
.next-race-card__live-video .next-race-card__live-video-icon {
  margin-bottom: -1px;
  fill: #7f7f7f;
}
.next-race-card__live-video.is-active .next-race-card__live-video-icon {
  margin-bottom: -1px;
  fill: #ef853f;
}
.next-race-card__status {
  display: block;
}
.next-race-card__race-status--inplay,
.next-race-card__status--race-status {
  white-space: nowrap;
  letter-spacing: 0.25px;
  font-size: 8px;
  line-height: 9px;
  color: #fff;
  text-transform: uppercase;
  display: inline-block;
  border-radius: 2px;
  padding: 3px 4px 2px;
}
.next-race-card__race-status--inplay {
  background-color: #20a052;
}
.next-race-card__status--race-status {
  background-color: #c2c2c2;
  margin-top: 6px;
}
.next-race-card__status--time {
  font-size: 9px;
  color: #7f7f7f;
  margin-right: 4px;
  white-space: nowrap;
}
.next-race-card__arrow {
  -ms-flex: 0 0 8px;
  flex: 0 0 8px;
  height: 8px;
  margin: -2px 0 0 7px;
}
.next-race-card__arrow .next-race-card__arrow-icon {
  width: 8px;
  height: 8px;
  fill: #303030;
  transform: rotate(180deg);
}
.bf-accordion {
  position: relative;
  width: 100%;
}
.bf-accordion .bf-section {
  padding-top: 1px;
}
.bf-accordion .bf-section-header {
  background-color: #303030;
  cursor: pointer;
  height: 24px;
  outline: 0;
}
.bf-accordion .bf-section-header:focus,
.bf-accordion .bf-section-header:hover {
  background: #1e1e1e;
}
.bf-accordion .bf-section-title {
  margin-left: 8px;
  float: left;
  line-height: 24px;
  color: #fff;
  font-weight: 700;
  font-size: 12px;
}
.bf-accordion .bf-section-toggle {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1913px;
  width: 11px;
  height: 7px;
  margin: 9px 8px 0;
  float: right;
  cursor: pointer;
}
.bf-accordion .bf-section-header.active .bf-section-toggle {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1923px;
}
.bf-accordion .bf-section-arrow {
  margin: 9px 8px 0;
  float: right;
  cursor: pointer;
  transition: all 0.2s ease;
}
.bf-accordion .bf-section-header.active .bf-section-arrow {
  transform: rotate(-180deg);
}
.bf-accordion .bf-section-content {
  transition: all 300ms ease-in-out;
  max-height: 0;
  overflow: hidden;
}
.bf-accordion .bf-section-content.active {
  display: block;
  max-height: 500px;
  opacity: 1;
}
.banner-directive {
  width: 100%;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.4);
}
.banner-directive .banner-container {
  margin: 0 auto;
}
.banner-directive .banner-image {
  width: 100%;
  min-height: 114px;
  margin: auto;
  display: block;
  border-radius: 2px 2px 0 0;
}
.banner-directive .banner-title {
  width: 100%;
  height: 28px;
  background-color: #303030;
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  text-align: left;
  vertical-align: middle;
  line-height: 28px;
  box-sizing: border-box;
  padding: 0 8px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.banner-directive .banner-subtitle {
  font-size: 14px;
  font-weight: 700;
  text-align: left;
  color: #1e1e1e;
  padding: 12px 8px 8px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.banner-directive .banner-links {
  padding: 0 8px 10px 0;
}
.banner-directive .banner-link {
  font-weight: 700;
  font-size: 12px;
  text-decoration: none;
  padding-left: 8px;
  line-height: 1.5;
  color: #167ac6;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: block;
}
.tab-navigation .tab-list .tab-title {
  line-height: 26px;
  float: left;
}
.tab-navigation .tab-content {
  float: left;
  width: 100%;
}
.svg-icon-default {
  width: 10px;
  height: 10px;
  color: #fff;
  fill: #fff;
}
.market-refresh-rate-container .label {
  vertical-align: middle;
  float: left;
  line-height: 18px;
  padding: 0;
}
.market-refresh-rate-container .value {
  float: left;
  width: 20px;
  padding: 0 4px;
  font-weight: 700;
  line-height: 18px;
}
.market-refresh-rate-container .market-refresh-rate-slider {
  width: 70px;
  display: inline-block;
  margin: 0 10px 0 5px;
  vertical-align: sub;
}
.market-refresh-rate-container .bf-slider {
  vertical-align: middle;
}
.market-refresh-rate-container input[type="range"]::-webkit-slider-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.market-refresh-rate-container input[type="range"]::-moz-range-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.market-refresh-rate-container input[type="range"]::-ms-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.module-loading-spinner::before {
  content: "";
  position: relative;
  width: 100%;
  display: block;
  float: none;
  z-index: 10;
  background-image: url(images/app/common/assets/images/betslip_spinner_4627_.gif);
  background-repeat: no-repeat;
  background-position: center center;
  background-color: #fff;
  background-position-y: 100px;
  border-right: 1px solid #bfbfbf;
}
.default-stake-preference input[type="checkbox"] {
  cursor: pointer;
  vertical-align: middle;
}
.default-stake-preference label {
  cursor: pointer;
  padding-left: 4px;
  vertical-align: middle;
}
.default-stakes-container .button-edit,
.default-stakes-container .button-set {
  padding: 0 8px;
  margin-left: 5px;
  height: 16px;
  line-height: 16px;
  border: 0;
  cursor: pointer;
  text-align: center;
  display: inline-block;
  border-radius: 2px;
  color: #1e1e1e;
  outline: 0;
}
.default-stakes-container .button-set {
  background-color: #ffb900;
}
.default-stakes-container .button-edit {
  background-color: #bfbfbf;
}
.default-stakes-container .default-stake .editable,
.default-stakes-container .default-stake .read-only {
  margin-right: 4px;
  height: 16px;
  line-height: 16px;
  width: 76px;
  cursor: pointer;
  text-align: center;
  display: inline-block;
  border-radius: 2px;
}
.default-stakes-container .default-stake .read-only {
  color: #1e1e1e;
  background-color: #e4e4e4;
}
.default-stakes-container .default-stake.active .read-only {
  color: #fff;
  background-color: #333;
}
.default-stakes-container .default-stake .editable {
  height: 14px;
  width: 62px;
  cursor: text;
  outline: 0;
  border: 1px solid #dfdfdf;
  background-color: #fff;
}
.default-stakes-container .default-stake .editable:focus {
  border: 1px solid #3d8acf;
}
.default-stakes-container .default-stake .error-message .bf-tooltip {
  background: #f33;
  box-shadow: none;
  margin-bottom: 8px;
  margin-left: 20px;
  height: 25px;
  border-radius: 2px;
  padding: 8px 0 8px 8px;
}
.default-stakes-container .default-stake .error-message .bf-tooltip::after {
  background: #f33;
  border: 1px solid #f33;
}
.default-stakes-container .default-stake .error-message .bf-tooltip .text {
  line-height: 13px;
  font-size: 11px;
  color: #fff;
}
.default-stakes-container
  .default-stake
  .error-message
  .bf-tooltip.has-close-button {
  width: 178px;
  border-left: 1px solid #fff;
}
.default-stakes-container
  .default-stake
  .error-message
  .bf-tooltip.has-close-button
  .text {
  padding-right: 4px;
  border-right: 1px solid #f66;
}
.default-stakes-container
  .default-stake
  .error-message
  .bf-tooltip.has-close-button
  .close-button::before {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 6px -1984px;
  width: 14px;
  height: 14px;
  content: " ";
  top: 6px;
}
.default-stakes-container
  .default-stake
  .error-message
  .bf-tooltip.has-close-button
  .close-button::after,
.default-stakes-container
  .default-stake
  .error-message
  .bf-tooltip.has-close-button
  .close-button::before {
  transform: none;
}
.default-stakes-container
  .default-stake
  .error-message
  .bf-tooltip.has-close-button
  .close-button::after {
  content: none;
}
.modal-dialog .hidden {
  display: none;
}
.modal-dialog .overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 101;
  background-color: rgba(17, 17, 17, 0.8);
  display: table;
}
.modal-dialog .overlay .dialog-container {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
.modal-dialog .overlay .dialog-container .dialog {
  padding: 0;
  height: auto;
  display: inline-block;
  vertical-align: top;
  background-color: #fff;
  box-shadow: 4px 3px 40px #000;
  position: relative;
  text-align: left;
  overflow: hidden;
  color: #444;
}
.modal-dialog .overlay .dialog-container .dialog-header {
  background: #dfdfdf;
  color: #1e1e1e;
  padding: 0 16px;
  height: 32px;
}
.modal-dialog .overlay .dialog-container .dialog-header .dialog-title {
  font-size: 14px;
  font-weight: 700;
  line-height: 32px;
}
.modal-dialog .overlay .dialog-container .dialog-header .close-dialog {
  position: absolute;
  top: 10px;
  right: 16px;
  cursor: pointer;
  width: 10px;
  height: 10px;
  padding: 2px;
  border-radius: 0;
  background: url(images/app/common/assets/svgs/modal-dialog/close-normal_4627_.svg)
    0 0 no-repeat;
}
.modal-dialog .overlay .dialog-container .dialog-header .close-dialog:hover {
  background: url(images/app/common/assets/svgs/modal-dialog/close-active_4627_.svg)
    0 0 no-repeat;
}
.modal-dialog .overlay .dialog-container .dialog-content {
  padding: 16px;
  font-size: 11px;
}
.modal-dialog .overlay .dialog-container .dialog-buttons {
  margin: 0 auto;
  display: block;
  width: auto;
  text-align: center;
  position: relative;
  padding: 10px;
}
.modal-dialog .overlay .dialog-container .dialog-buttons .dialog-button {
  cursor: pointer;
  color: #444;
  font-weight: 700;
  border-radius: 4px;
  border-width: 1px;
  border-color: #eee #eee #bbb;
  padding: 4px 6px;
  background: linear-gradient(0deg, #fff, #eaeff2);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#eaeff2", endColorstr="white", GradientType=0);
}
.bf-overlay {
  position: absolute;
  left: -4px;
  right: -4px;
  top: -4px;
  bottom: -4px;
  background-color: #fff;
  background-color: transparent\9;
  background-color: hsla(0, 0%, 100%, 0.9);
  z-index: 100;
}
.overlayPosition {
  position: relative;
}
.rating {
  overflow: hidden;
}
.rating .star {
  float: left;
  margin-right: 5px;
  color: #a5a4aa;
}
.rating .star .selected {
  color: #a71b62;
}
.suspended-overlay-active .mv-bet-button,
.suspended-overlay-active .sp-odds,
.suspended-overlay-active button.suspended {
  opacity: 0.5;
}
.suspended-overlay-container {
  position: absolute;
  z-index: 10;
  display: none;
  overflow: auto;
  top: 6%;
}
.suspended-overlay-container.suspended {
  display: table;
}
.suspended-overlay-container .suspended-overlay-wrapper .suspended-label {
  font-size: 18px;
  font-weight: 700;
  padding: 8px 36px 11px;
  color: #b30000;
  background-color: rgba(255, 255, 255, 0.65);
  border: 2px solid #b30000;
  text-align: center;
  display: inline-block;
  margin: 0 auto;
  position: absolute;
  top: 40%;
  left: 40%;
}
.show-ah-summary ~ .suspended-overlay-container.suspended {
  top: 25%;
}
.average__odds {
  border-top: 1px solid #fff;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
.average__odds--back {
  background-color: #dbefff;
}
.average__odds--lay {
  background-color: #fee9ee;
}
.average__odds--text {
  color: #273a47;
  padding: 7px 6px;
  margin-right: 80px;
  text-align: right;
  font-weight: 700;
}
.average__odds--total_stake {
  color: #273a47;
  padding: 7px;
}
.bet-placed-information__container {
  box-sizing: border-box;
  color: #7f7f7f;
  padding: 2px 8px;
  font-size: 10px;
}
.bet-placed-information__reference {
  margin-right: 8px;
}
.bet-placed-information__element {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}
.bet-placed-information__bonus-icon {
  background: transparent
    url(images/app/common/assets/svgs/betslip/bonus-icon_4627_.svg) no-repeat
    center;
  display: inline-block;
  width: 16px;
  height: 16px;
  margin-right: 5px;
}
.bet-report {
  padding: 0 8px 8px;
}
.betslip-bet {
  border-bottom: 1px solid #ebebeb;
}
.betslip-bet--BACK,
.betslip-bet--back {
  background-color: #dbefff;
  border-bottom: 1px solid #fff;
}
.betslip-bet--LAY,
.betslip-bet--lay {
  background-color: #fee9ee;
  border-bottom: 1px solid #fff;
}
.betslip-bet__container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
  padding: 8px 4px;
}
.betslip-bet__item {
  box-sizing: border-box;
  padding: 0 4px;
}
.betslip-bet__runner-name {
  font-weight: 700;
}
.betslip-bet__runner-details {
  display: -ms-flexbox;
  display: flex;
}
.betslip-bet__runner-detail {
  text-align: center;
  width: 64px;
}
.betslip-bet__error-message {
  display: block;
  padding: 0 8px 8px;
}
.betslip-bet__placed-information {
  padding-bottom: 5px;
}
.betslip-bets-header-ordered {
  padding: 3px;
  width: 100%;
  box-sizing: border-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -ms-flex-align: center;
  align-items: center;
}
.betslip-bets-header-ordered__values {
  display: -ms-flexbox;
  display: flex;
}
.betslip-bets-header-ordered__cell {
  padding: 2px 4px;
  box-sizing: border-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
}
.betslip-bets-header-ordered__cell--fixed-size {
  text-align: center;
  width: 64px;
}
.betslip-bets-header {
  padding: 4px;
  width: 100%;
  box-sizing: border-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -ms-flex-align: center;
  align-items: center;
}
.betslip-bets-header--under {
  background: #51ad95;
  color: #fff;
}
.betslip-bets-header--over {
  background: #519995;
  color: #fff;
}
.betslip-bets-header--back {
  background-color: #a6d8ff;
}
.betslip-bets-header--lay {
  background-color: #fac9d4;
}
.betslip-bets-header__values {
  display: -ms-flexbox;
  display: flex;
  position: relative;
}
.betslip-bets-header__cell {
  padding: 2px 4px;
  box-sizing: border-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
}
.betslip-bets-header__cell--fixed-size {
  text-align: center;
  width: 64px;
  word-break: break-word;
  overflow-wrap: break-word;
}
.betslip-bets-header-link--back {
  color: #2789ce;
  cursor: pointer;
}
.betslip-bets-header__options {
  text-align: left;
  padding-top: 2px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  margin-right: 10px;
}
.betslip-bets-header__radio-button {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  height: 14px;
  width: 55px;
}
.betslip-bets-header__radio-liability,
.betslip-bets-header__radio-payout {
  background-size: 10px;
  width: 11px;
  height: 10px;
  vertical-align: top;
  margin: 1px 2px;
}
.betslip-bets-header__dutching-link {
  cursor: pointer;
  color: #2789ce;
}
.betslip-bets-header__dutching-interrogation {
  cursor: help;
  color: #2789ce;
}
.betslip-bets-header__dutching-helper-back {
  width: 13px;
  height: 13px;
  cursor: help;
  padding-left: 1px;
}
.betslip-bets-header__dutching-helper-lay {
  width: 10px;
  height: 13px;
  cursor: help;
  position: absolute;
  right: 0;
}
.bets-state-header {
  background-color: #303030;
  color: #fff;
  font-size: 1.2rem;
  padding: 8px;
  position: relative;
}
.bets-state-header__title {
  font-weight: 700;
}
.bets-state-header__description {
  margin-top: 6px;
  font-size: 1.1rem;
}
.bets-state-header__odds-limit,
.bets-state-header__orderby {
  position: absolute;
  right: 0;
  margin-top: 8px;
  top: 0;
  overflow: hidden;
  white-space: nowrap;
  margin-right: 7px;
  text-overflow: ellipsis;
  font-size: 1.1rem;
}
.bets-state-header__orderby {
  max-width: 180px;
}
.bets-state-header__odds-limit {
  max-width: 130px;
}
.confirmation-footer {
  background-color: #ebebeb;
  padding: 4px;
}
.confirmation-footer__actions {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
  padding: 4px;
}
.confirmation-footer__liability {
  -ms-flex: 1;
  flex: 1;
  font-size: 12px;
  color: #273a47;
  text-align: right;
}
.confirmation-footer__liability--value {
  font-weight: 700;
}
.confirmation-footer__total-values {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding: 2px 7px 10px;
}
.dutching-information-modal .dialog {
  width: 300px;
}
.dutching-information-modal__first-part {
  margin-bottom: 10px;
}
.dutching-popup {
  background: #fff9d8;
  border: 1px solid #7d97a8;
  padding: 8px;
}
.dutching-popup__info {
  color: #273a47;
  font-weight: 700;
  margin-bottom: 3px;
  font-size: 1.1rem;
}
.dutching-popup__container {
  overflow: auto;
}
.dutching-popup__label {
  line-height: 19px;
  display: -ms-inline-flexbox;
  display: inline-flex;
}
.dutching-popup__button {
  font-weight: 700;
  font-size: 1.1rem;
  text-align: center;
  line-height: 16px;
  height: 18px;
  padding: 0 10px;
  background-color: #cbcbcb;
  border-bottom: 1px solid #94a8b3;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
}
.dutching-popup__button:focus {
  box-shadow: inset 0 2px 5px 2px rgba(0, 0, 0, 0.2);
  border: 0;
}
.dutching-popup__input {
  width: 50px;
  height: 18px;
  border: 1px solid #e0e6e6;
  text-align: center;
  font-size: 1.1rem;
  font-weight: 400;
  color: #273a47;
  margin-right: 4px;
  margin-left: 8px;
}
.betslip__editable-bet {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: justify;
  justify-content: space-between;
  box-sizing: border-box;
  width: 100%;
  padding: 4px;
}
.betslip__editable-bet__container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}
.betslip__editable-bet__item {
  box-sizing: border-box;
  padding: 0 4px;
}
.betslip__editable-bet__runner {
  font-weight: 700;
}
.betslip__editable-bet__cell {
  width: 64px;
  text-align: center;
}
.betslip__editable-bet--back {
  background-color: #dbefff;
}
.betslip__editable-bet--lay {
  background-color: #fee9ee;
}
.betslip__editable-sp-bet {
  -ms-flex-align: center;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
}
.betslip__editable-sp-bet__container {
  -ms-flex-pack: justify;
  justify-content: space-between;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding: 3px 2px 2px 4px;
}
.betslip__editable-sp-bet__item {
  box-sizing: border-box;
  padding: 0 4px;
}
.betslip__editable-sp-bet__runner {
  font-weight: 700;
}
.betslip__editable-sp-bet__cell {
  width: 64px;
  text-align: center;
}
.betslip__editable-sp-bet--back {
  background-color: #dbefff;
}
.betslip__editable-sp-bet--lay {
  background-color: #fee9ee;
}
.betslip__editable-sp-bet__placed-information {
  padding-bottom: 5px;
}
.error-message__statement {
  font-weight: 700;
  font-size: 1.1rem;
  color: #bc4848;
}
.error-message__link {
  color: #2797e6;
  cursor: pointer;
}
.free-bets-label {
  color: #303030;
  font-size: 12px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  background-color: #ebebeb;
}
.free-bets-label--large {
  padding: 12px 8px;
}
.free-bets-label__bonus-icon {
  background: transparent
    url(images/app/common/assets/svgs/betslip/bonus-icon_4627_.svg) no-repeat
    center;
  display: inline-block;
  width: 16px;
  height: 16px;
  margin-right: 5px;
}
.free-bets-label__bonus-text {
  margin-left: 2px;
}
.free-bets-toggle {
  padding: 4px;
  color: #303030;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
.free-bets-toggle__bonus-icon {
  background: transparent
    url(images/app/common/assets/svgs/betslip/bonus-icon_4627_.svg) no-repeat
    center;
  display: inline-block;
  width: 16px;
  height: 16px;
  margin-right: 5px;
}
.free-bets-toggle__bonus-text {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}
.free-bets-toggle__hr {
  height: 1px;
  color: #dcdcdc;
  background-color: #dcdcdc;
  border: 0;
  margin: 2px 4px 5px;
}
.free-bets-toggle__error {
  font-size: 12px;
  color: #626262;
  padding: 4px 4px 10px;
}
.betslip__header {
  border-bottom: 1px solid #dcdcdc;
  padding: 8px;
  position: relative;
}
.betslip__header__title {
  font-size: 1.4rem;
  font-weight: 700;
}
.inplay-options {
  margin-top: 3px;
}
.inplay-options__title {
  font-size: 1.1rem;
  font-weight: 700;
}
.inplay-options__item {
  margin: 0 3px;
  line-height: 1.3rem;
}
.loading-component {
  background-color: #fff;
  -ms-flex-align: center;
  align-items: center;
  height: 80px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: center;
  justify-content: center;
}
.loading-component__text {
  font-weight: 700;
  font-size: 12px;
}
.open-footer {
  background-color: #ebebeb;
  padding: 6px 6px 12px;
  border-top: 1px solid #fff;
}
.open-footer__actions {
  display: -ms-flexbox;
  display: flex;
  margin-bottom: 8px;
}
.open-footer__action {
  padding: 4px;
}
.open-footer__right-actions {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: end;
  justify-content: flex-end;
  -ms-flex: 1;
  flex: 1;
}
.open-footer__options {
  display: -ms-flexbox;
  display: flex;
  padding: 4px 2px;
}
.open-footer__option {
  padding: 0 4px;
  display: inherit;
}
.open-footer__option__input {
  margin-right: 4px;
}
.pnl-container {
  padding: 4px;
  min-height: 38px;
}
.pnl__row {
  padding: 4px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
.pnl__row--invisible {
  visibility: hidden;
}
.pnl__value {
  color: #bc4848;
}
.pnl__value--positive {
  color: #006700;
}
.potentials-footer {
  background-color: #ebebeb;
  padding: 4px;
}
.potentials-footer__actions {
  display: -ms-flexbox;
  display: flex;
}
.potentials-footer__action {
  padding: 4px;
}
.potentials-footer__options {
  padding: 8px 4px;
}
.potentials-footer__options > label {
  margin-right: 15px;
  display: inline-block;
  line-height: 2rem;
}
.potentials-footer__option {
  margin-right: 4px;
}
.potentials-footer__right-actions {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: end;
  justify-content: flex-end;
  -ms-flex: 1;
  flex: 1;
}
.potentials-footer__liability {
  display: -ms-flexbox;
  display: flex;
  text-align: right;
  font-size: 12px;
  color: #273a47;
  padding: 7px;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
.potentials-footer__liability--value {
  font-weight: 700;
}
.potentials-footer__liability--stripe {
  text-decoration: line-through;
}
.potentials-footer__using-bonus {
  color: #7f7f7f;
  font-size: 11px;
  text-align: left;
  width: 100%;
}
.potentials-footer__liability--text--value {
  text-align: right;
  width: 100%;
}
.betslip-price-ladder {
  position: relative;
}
.betslip-price-ladder__input {
  padding: 2px 14px 2px 0;
  border: 1px solid #dcdcdc;
  text-align: center;
  width: 100%;
  box-sizing: border-box;
}
.betslip-price-ladder__input--invalid {
  border: 1px solid #bc4848;
}
.betslip-price-ladder__buttons {
  position: absolute;
  top: 0;
  right: 6px;
  height: 100%;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  -ms-flex-pack: distribute;
  justify-content: space-around;
  box-sizing: border-box;
  padding: 1px 0;
}
.betslip-price-ladder__button {
  width: 8px;
  height: 4px;
  padding: 0;
  border: 0;
}
.betslip-price-ladder__button:disabled {
  opacity: 0.5;
}
.betslip-price-ladder__arrow-up {
  background: transparent
    url(images/app/common/assets/svgs/betslip/nudge-arrow_4627_.svg) no-repeat
    center;
}
.betslip-price-ladder__arrow-down {
  background: transparent
    url(images/app/common/assets/svgs/betslip/nudge-arrow_4627_.svg) no-repeat
    center;
  transform: rotate(180deg);
}
.receipt-footer {
  background-color: #ebebeb;
  padding: 4px;
}
.receipt-footer__actions {
  display: -ms-flexbox;
  display: flex;
}
.receipt-footer__action {
  display: block;
  padding: 4px;
}
.receipt-footer__options {
  padding: 8px 4px;
}
.receipt-footer__option {
  margin-right: 4px;
}
.receipt-footer__right-actions {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: end;
  justify-content: flex-end;
  -ms-flex-align: end;
  align-items: flex-end;
  -ms-flex: 1;
  flex: 1;
}
.receipt-footer__cancel-unmatched {
  width: 150px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  display: block;
}
.betslip-refresh-button {
  background-color: #303030;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  color: #fff;
  padding: 0 10px;
  cursor: pointer;
  font-size: 1.1rem;
  line-height: 1.6rem;
  position: absolute;
  top: 0;
  right: 0;
  margin: 7px 4px 5px;
  border: 0;
  outline: 0;
}
.betslip-refresh-button:active {
  background-color: #000;
  color: #7e97a7;
}
.betslip-size-input {
  padding: 2px 0;
  border: 1px solid #dcdcdc;
  text-align: center;
  width: 100%;
  box-sizing: border-box;
}
.betslip-size-input--invalid {
  border: 1px solid #bc4848;
}
.betslip-sp-bet {
  border-bottom: 1px solid #ebebeb;
}
.betslip-sp-bet--BACK,
.betslip-sp-bet--back {
  background-color: #dbefff;
  border-bottom: 1px solid #fff;
}
.betslip-sp-bet--LAY,
.betslip-sp-bet--lay {
  background-color: #fee9ee;
  border-bottom: 1px solid #fff;
}
.betslip-sp-bet__container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
  padding: 8px 4px;
}
.betslip-sp-bet__item {
  box-sizing: border-box;
  padding: 0 4px;
}
.betslip-sp-bet__runner-name {
  font-weight: 700;
}
.betslip-sp-bet__runner-details {
  display: -ms-flexbox;
  display: flex;
}
.betslip-sp-bet__runner-detail {
  text-align: center;
  width: 64px;
}
.betslip-sp-bet__error-message {
  display: block;
  padding-right: 8px;
  padding-bottom: 8px;
  padding-left: 8px;
}
.betslip-sp-bets-header {
  padding: 5px 4px;
  width: 100%;
  box-sizing: border-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -ms-flex-align: center;
  align-items: center;
}
.betslip-sp-bets-header--back {
  background-color: #a6d8ff;
}
.betslip-sp-bets-header--lay {
  background-color: #fac9d4;
}
.betslip-sp-bets-header__values {
  display: -ms-flexbox;
  display: flex;
}
.betslip-sp-bets-header__cell {
  padding: 2px 4px;
  box-sizing: border-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
}
.betslip-sp-bets-header__cell--fixed-size {
  text-align: center;
  width: 64px;
  word-break: break-word;
}
.popup__container {
  width: 100%;
  height: 100%;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
}
.popup__content {
  width: auto;
  height: auto;
  position: absolute;
}
@keyframes spinning {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
.bf-spinner {
  width: 30px;
  height: 30px;
  margin: 0 auto;
  background: transparent
    url(images/app/common/assets/svgs/betslip/spinner_4627_.svg) no-repeat;
  animation: 1s steps(12, end) infinite spinning;
}
.betslip-container bf-tabs .XSELL {
  float: right;
  background: transparent
    url(images/app/common/assets/svgs/betslip/arcade-icon_4627_.svg) 12px 6px
    no-repeat;
  border-left: 1px solid #dfdfdf;
  max-width: 110px;
  padding-left: 15px;
}
.betslip-container .tabs-container {
  height: 28px;
}
.betslip-container .tabs-container .tab-heading {
  padding: 0 16px;
}
.betslip-container .tabs-container .tab-heading .tab-label {
  font-size: 11px;
}
.login-link {
  color: #2789ce;
  text-decoration: none;
  cursor: pointer;
}
.betslip-confirmation__sub-title {
  padding-top: 8px;
}
.betslip-confirmation__link {
  color: #2797e6;
}
.betslip-countdown {
  position: relative;
  top: 65px;
}
.betslip-countdown__spinner {
  display: block;
}
.betslip-countdown__placeholder {
  font-weight: 700;
  font-size: 11px;
  text-align: center;
  margin-top: 15px;
}
.betslip-countdown__timer {
  font-weight: 700;
  font-size: 9px;
  text-align: center;
  margin-top: 10px;
}
.empty-state {
  margin-top: 40px;
  text-align: center;
}
.empty-state__message {
  font-weight: 700;
  margin-bottom: 12px;
}
.empty-state__button-sbw-multiples {
  cursor: pointer;
  border-radius: 2px;
  margin: 13px 0;
  min-height: 18px;
  padding: 4px 8px;
  line-height: 18px;
  text-align: center;
  text-decoration: none;
  font-size: 11px;
  display: inline-block;
  color: #1e1e1e;
  background: #ffb900;
}
.empty-state__button-sbw-multiples .empty-state__button-sbw-multiples-bold {
  font-weight: 700;
}
.games-container {
  position: absolute;
  background-color: #fff;
  top: 30px;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 0 40px;
  overflow: scroll;
}
.games-container .games-mini-header {
  margin: 8px 0 9px 8px;
  font-size: 11px;
  font-weight: 700;
}
.games-container .games-content {
  transition: all 300ms ease-in-out;
  -moz-transition: all 300ms ease-in-out;
  -webkit-transition: all 300ms ease-in-out;
  opacity: 1;
  overflow: hidden;
  background-color: #fff;
  position: absolute;
  display: block;
  margin: 0 auto;
  text-align: center;
  top: 30px;
  bottom: 0;
  left: 0;
}
.games-container .games-content .games-item {
  margin: 8px 0;
  overflow: hidden;
  float: left;
  width: 49%;
  text-align: center;
  cursor: pointer;
}
.games-container .games-content .games-item:first-child {
  margin-left: 3.5%;
}
.games-container .games-content .games-item:last-child {
  margin-left: -3.5%;
}
.open-sp-bet__editable {
  border-bottom: 1px solid #fff;
  display: block;
}
.bets-container__unmatched-fallback {
  background-color: #fff;
  padding: 12px 8px;
  text-align: center;
  font-weight: 700;
}
.betslip__unmatched-bet {
  padding-bottom: 8px;
  border-bottom: 1px solid #fff;
}
.betslip__unmatched-bet--back {
  background-color: #dbefff;
}
.betslip__unmatched-bet--lay {
  background-color: #fee9ee;
}
.betslip__unmatched-bet--over,
.betslip__unmatched-bet--under {
  border-bottom: 1px solid #ebebeb;
}
.betslip__bet-inplay-options {
  display: block;
  margin: 0 8px;
}
.betslip-potentials__error-message {
  display: block;
  padding-top: 8px;
}
.receipt__matched-bets .free-bets-label,
.receipt__sp-bets .free-bets-label,
.receipt__unmatched-bets .free-bets-label {
  padding: 12px 10px;
  border-bottom: 1px solid #fff;
}
.cashout-page {
  overflow: auto;
  max-height: 100vh;
}
.cashout-page__container .bf-livescores {
  min-width: auto;
}
.cashout-page__container .cashout-markets-tab-content {
  margin: 8px 0 0;
}
.cashout-page__container .cashout-markets-tab-content .column-left,
.cashout-page__container .cashout-markets-tab-content .column-right {
  width: calc(50% - 4px);
}
.cashout-page__container .cashout-markets-tab-content .column-left {
  float: left;
}
.cashout-page__container .cashout-markets-tab-content .column-right {
  float: right;
}
.cashout-page__container .marketview-header-wrapper-bottom-container {
  padding-top: 0;
}
.cashout-page__container .mini-mv,
.cashout-page__container .mini-mv .mv-header-main-section-wrapper {
  background-color: #fff;
}
.cashout-page__container .mini-mv .expand-collapse-link,
.cashout-page__container .mini-mv .mini-mv-full-market-link {
  height: 28px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}
.cashout-page__container .mini-mv .mini-mv-full-market-link {
  -ms-flex-pack: end;
  justify-content: flex-end;
  margin: 0 8px 0 0;
}
.cashout-page__container .mini-mv .expand-collapse-link {
  -ms-flex-pack: center;
  justify-content: center;
  margin: 0;
}
.cashout-page__container .mod-cashout {
  border-bottom: 1px solid #dfdfdf;
}
.cashout-info-box__container {
  background-color: #fff;
  padding: 8px;
  margin-top: 8px;
  color: #303030;
  font-size: 12px;
}
.logged-out-description__container--paragraph {
  line-height: 16px;
}
.logged-out-description__container--paragraph:first-child {
  margin-bottom: 16px;
}
.cashout-help__link {
  color: #0678c9;
  text-decoration: underline;
  font-weight: 700;
}
.logged-out-login__container,
.no-cashout__container {
  font-weight: 700;
  text-align: center;
  line-height: 16px;
  font-size: 10px;
}
.logged-out-login__container {
  margin-top: 1px;
}
.mini-mv__fake-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  background-color: #fff;
  margin-bottom: 8px;
}
.mini-mv__fake-livescores {
  background-color: #acacac;
  height: 50px;
}
.mini-mv__fake-header {
  border-bottom: 1px solid #f4f4f4;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
.mini-mv__fake-header__text {
  background-color: #f4f4f4;
  width: 80px;
  height: 15px;
  margin: 8px 10px;
}
.mini-mv__fake-header__buttons {
  display: -ms-flexbox;
  display: flex;
}
.mini-mv__fake-header__buttons__button {
  background-color: #f4f4f4;
  width: 16px;
  height: 16px;
  margin: 8px 4px;
}
.mini-mv__fake-header__buttons__button_large {
  background-color: #f4f4f4;
  width: 53px;
  height: 16px;
  margin: 8px 4px;
}
.mini-mv__fake-cashout {
  height: 54px;
}
.mini-mv__fake-runners {
  border-bottom: 1px solid #f4f4f4;
}
.mini-mv__fake-runners__text {
  height: 13px;
  background-color: #f4f4f4;
  margin: 8px auto;
  width: 100px;
}
.mini-mv__fake-full-market {
  height: 13px;
  background-color: #f4f4f4;
  margin: 8px 10px 8px auto;
  width: 100px;
}
.full-height-page,
.full-height-page > div {
  height: 100%;
}
.mod-404 {
  background-image: url(images/app/common/assets/images/404-error-page_4627_.jpg);
  width: 100%;
  height: 100%;
  display: table;
  background-position: left top;
}
.mod-404 .content-holder-404 {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
.mod-404 .content-holder-404 .content-404 {
  width: 656px;
  display: inline-block;
  text-align: left;
}
.mod-404 .content-holder-404 .content-404 .top-section {
  color: #fff;
  position: relative;
}
.mod-404 .content-holder-404 .content-404 .top-section .title {
  font-family: BlockBESmoothRegular, sans-serif;
  font-size: 94px;
  line-height: 84px;
  padding: 45px;
  text-transform: uppercase;
}
.mod-404 .content-holder-404 .content-404 .top-section .frame-top-right {
  background: transparent url(images/app/common/assets/svgs/404/frame_4627_.svg)
    0 0 no-repeat;
  width: 80px;
  height: 80px;
  position: absolute;
  right: 0;
  top: 0;
  transform: rotate(180deg);
}
.mod-404 .content-holder-404 .content-404 .top-section .frame-bottom-left {
  background: transparent url(images/app/common/assets/svgs/404/frame_4627_.svg)
    0 0 no-repeat;
  width: 80px;
  height: 80px;
  position: absolute;
  left: 0;
  bottom: 0;
}
.mod-404 .content-holder-404 .content-404 .content {
  color: #fff;
  text-align: center;
  margin-top: 30px;
}
.mod-404 .content-holder-404 .content-404 .content .title {
  font-family: BlockBESmoothRegular, sans-serif;
  font-size: 46px;
  text-transform: uppercase;
}
.mod-404 .content-holder-404 .content-404 .content .message {
  font-family: BlockBESmoothRegular, sans-serif;
  font-size: 18px;
  line-height: 24px;
  text-align: justify;
  padding: 0 60px;
  text-transform: uppercase;
}
.mod-404 .content-holder-404 .content-404 .buttons {
  margin: 0 0 10px;
  overflow: auto;
  display: flex;
  display: -ms-flexbox;
  -ms-flex-pack: center;
  justify-content: center;
  align-items: center;
  -ms-flex-align: center;
}
.mod-404 .content-holder-404 .content-404 .buttons .button-404 {
  float: left;
  background-color: transparent;
  border: 2px solid #fff;
  color: #fff;
  font-weight: 700;
  font-size: 14px;
  text-align: center;
  width: 188px;
  text-decoration: none;
  padding: 0 10px;
  line-height: 40px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  border-radius: 2px;
  margin-left: 10px;
}
.mod-404 .content-holder-404 .content-404 .buttons > .button-404:first-child {
  margin-left: 0;
}
.mod-404 .content-holder-404 .content-404 .buttons .button-404:hover {
  color: #000;
  background-color: #fff;
}
.mod-404 .content-holder-404 .content-404 .buttons.static {
  margin-top: 30px;
}
.ah-pnl-table-single-line-container {
  height: 214px;
}
.ah-pnl-table-single-line-container table {
  width: 100%;
}
.ah-pnl-table-single-line-container td,
.ah-pnl-table-single-line-container th {
  margin: 0 10px;
  padding: 4px 8px;
  color: #1e1e1e;
  font-size: 11px;
  line-height: 16px;
  border-bottom: 1px solid #dfdfdf;
}
.ah-pnl-table-single-line-container th {
  background-color: #d9d9d9;
  border-bottom: 0;
}
.ah-pnl-table-single-line-container th:nth-child(1) {
  width: 52%;
}
.ah-pnl-table-single-line-container th:nth-child(2),
.ah-pnl-table-single-line-container th:nth-child(3) {
  width: 24%;
}
.ah-pnl-table-single-line-container .pnl-table-content td:nth-child(1) {
  padding-left: 0;
  width: 54%;
}
.ah-pnl-table-single-line-container .pnl-table-content td:nth-child(2) {
  width: 26.5%;
}
.ah-pnl-table-single-line-container .pnl-table-content td:nth-child(3) {
  padding-right: 0;
  width: 19.5%;
}
.ah-pnl-table-single-line-container .pnl-table-content-wrapper {
  height: 190px;
  overflow-y: scroll;
  padding: 0 8px;
}
.ah-pnl-table-single-line-container .pnl-table-content-wrapper.empty {
  height: auto;
  overflow: auto;
}
.ah-pnl-table-single-line-container
  .pnl-table-content-wrapper.empty
  td:nth-child(1) {
  padding-left: 0;
  width: 52%;
}
.ah-pnl-table-single-line-container
  .pnl-table-content-wrapper.empty
  td:nth-child(2) {
  width: 25.5%;
}
.ah-pnl-table-single-line-container
  .pnl-table-content-wrapper.empty
  td:nth-child(3) {
  padding-right: 0;
  width: 22.5%;
}
.ah-pnl-table-single-line-container .negative {
  color: #b30000;
}
.ah-pnl-table-single-line-container .empty-result {
  font-size: 12px;
  line-height: 16px;
  font-weight: 700;
  margin: 66px 55px 0;
  text-align: center;
}
html[lang="bg-bg"]
  .ah-pnl-table-single-line-container
  .pnl-table-content-wrapper,
html[lang="de-de"]
  .ah-pnl-table-single-line-container
  .pnl-table-content-wrapper,
html[lang="el-gr"]
  .ah-pnl-table-single-line-container
  .pnl-table-content-wrapper,
html[lang="it-it"]
  .ah-pnl-table-single-line-container
  .pnl-table-content-wrapper,
html[lang="ru-ru"]
  .ah-pnl-table-single-line-container
  .pnl-table-content-wrapper {
  height: 174px;
}
body:not(:-moz-handler-blocked)
  .ah-pnl-table-single-line-container
  .pnl-table-content-wrapper {
  padding-right: 25px;
}
body:not(:-moz-handler-blocked)
  .ah-pnl-table-single-line-container
  .pnl-table-content-wrapper.empty {
  padding-right: 8px;
}
body:not(:-moz-handler-blocked)
  .ah-pnl-table-single-line-container
  th:nth-child(2) {
  width: 24.5%;
}
.bf-row-aside {
  position: absolute;
  bottom: 0;
  top: 0;
  right: 0;
}
.aside-bottom-row {
  width: 100%;
}
.betslip-view .potential-container .back {
  min-height: 80px;
}
.betslip-view .potential-container .lay {
  min-height: 91px;
}
.betslip-view .bets-container {
  transition: all 300ms ease-in-out;
  overflow-y: auto;
}
.betslip-view .bets-container-loading {
  margin: 10px 0;
  text-align: center;
  font-weight: 700;
  font-size: 12px;
  color: #273a47;
}
.betslip-view .bets-view-loading {
  margin: 30px 0;
  text-align: center;
  font-weight: 700;
  font-size: 12px;
  color: #273a47;
}
.betslip-view .scroll-wrapper {
  zoom: 1;
  overflow: auto;
}
.betslip-view .scroll-wrapper::after {
  content: ".";
  display: block;
  clear: both;
  overflow: hidden;
  line-height: 0;
  height: 0;
}
.betslip-view .confirmation-header {
  margin-left: 8px;
  overflow: auto;
}
.betslip-view .confirmation-header .market-confirmation-text {
  text-align: left;
  font-weight: 700;
  font-size: 14px;
  padding: 5px 8px 7px 0;
  color: #000;
}
.betslip-view .confirmation-header .market-comission-text {
  margin: 1px 0 8px;
  color: #273a47;
  font-size: 11px;
}
.betslip-view .confirmation-header .market-comission {
  text-decoration: underline;
  color: #2489d5;
  padding: 0;
  margin: 0;
  cursor: pointer;
}
.betslip-view .current-odds-title {
  float: left;
}
.betslip-view .current-odds-options {
  padding-top: 5px;
}
.betslip-view .current-odds-options .radio-btn-cancel-wrapper,
.betslip-view .current-odds-options .radio-btn-keep-wrapper,
.betslip-view .current-odds-options .radio-btn-take-sp-wrapper {
  float: left;
  margin-left: 10px;
  font-weight: 400;
}
.betslip-view .radio-btn-cancel-wrapper .radio-btn-cancel,
.betslip-view .radio-btn-keep-wrapper .radio-btn-keep,
.betslip-view .radio-btn-take-sp-wrapper .radio-btn-take-sp {
  vertical-align: top;
  margin: -1px 4px 0 0;
}
.betslip-view .current-odds-radio-btn {
  vertical-align: top;
}
.betslip-view .line-separator {
  height: 1px;
  background-color: #ced5e0;
  margin-bottom: 8px;
}
.betslip-view .line-separator.flat {
  margin-top: 0;
}
.betslip-view .bet-price {
  width: 53px;
  text-align: center;
  display: inline-block;
}
.betslip-view .bet-size {
  width: 55px;
  text-align: center;
  display: inline-block;
}
.betslip-view .bet-values .oddsladder {
  float: left;
  margin-right: 6px;
}
.betslip-view .sp-bet-wrapper .back-bet-text,
.betslip-view .sp-bet-wrapper .lay-bet-text {
  text-align: left;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.betslip-view .stake-text-wrapper {
  margin-right: 4px;
}
.betslip-view .stake-text-wrapper .stake-text {
  display: inline-block;
  line-height: 10px;
}
.betslip-view .stake-text-wrapper .stake-hint-wrapper {
  width: 13px;
  height: 16px;
  cursor: help;
}
.betslip-view .stake-text-wrapper .stake-text-handicaps {
  padding-right: 7px;
}
.betslip-view .bet-header {
  clear: both;
  min-height: 25px;
  overflow: auto;
}
.betslip-view .bet-header.back-bets-header {
  background-color: #a6d8ff;
  display: table;
  width: 100%;
}
.betslip-view .bet-header.back-bets-header .back-bets-header-wrapper {
  display: table-row;
}
.betslip-view .bet-header.lay-bets-header {
  background-color: #fac9d4;
  display: table;
  width: 100%;
  height: 36px;
}
.betslip-view .bet-header.lay-bets-header .lay-bets-header-wrapper {
  display: table-row;
}
.betslip-view .bet-header .header-item {
  display: inline-block;
  text-align: center;
  padding: 5px 8px;
  height: 13px;
}
.betslip-view .bet-header .back-bet-text,
.betslip-view .bet-header .backers-liability-text,
.betslip-view .bet-header .backers-odds-text,
.betslip-view .bet-header .backers-stake-text,
.betslip-view .bet-header .lay-bet-text,
.betslip-view .bet-header .odds-text,
.betslip-view .bet-header .profit-text {
  white-space: pre-wrap;
}
.betslip-view .bet-header .stake-text-link {
  cursor: pointer;
  color: #2789ce;
}
.betslip-view .bet-header .back-bet-text,
.betslip-view .bet-header .lay-bet-text {
  text-align: left;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  height: 15px;
  padding: 0 2px 0 8px;
  display: table-cell;
  vertical-align: middle;
}
.betslip-view .bet-header .odds-text {
  display: inline-block;
  text-align: center;
  line-height: 10px;
  width: 62px;
  white-space: pre-wrap;
}
.betslip-view .bet-header .stake-text {
  white-space: pre-wrap;
}
.betslip-view .bet-header .back-bet-text-wrapper,
.betslip-view .bet-header .bet-text-wrapper,
.betslip-view .bet-header .lay-bet-text-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.betslip-view .bet-header .back-bet-text-wrapper .back-bet-text,
.betslip-view .bet-header .back-bet-text-wrapper .lay-bet-text,
.betslip-view .bet-header .bet-text-wrapper .back-bet-text,
.betslip-view .bet-header .bet-text-wrapper .lay-bet-text,
.betslip-view .bet-header .lay-bet-text-wrapper .back-bet-text,
.betslip-view .bet-header .lay-bet-text-wrapper .lay-bet-text {
  min-height: 26px;
  padding: 0 2px 0 8px;
}
.betslip-view
  .bet-header
  .back-bet-text-wrapper
  .back-bet-text.has-sp-odds-limit,
.betslip-view
  .bet-header
  .back-bet-text-wrapper
  .lay-bet-text.has-sp-odds-limit,
.betslip-view .bet-header .bet-text-wrapper .back-bet-text.has-sp-odds-limit,
.betslip-view .bet-header .bet-text-wrapper .lay-bet-text.has-sp-odds-limit,
.betslip-view
  .bet-header
  .lay-bet-text-wrapper
  .back-bet-text.has-sp-odds-limit,
.betslip-view
  .bet-header
  .lay-bet-text-wrapper
  .lay-bet-text.has-sp-odds-limit {
  line-height: 28px;
  height: 28px;
  padding-top: 0;
  padding-bottom: 0;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  width: 60px;
}
.betslip-view .bet-header .back-odds-text-wrapper,
.betslip-view .bet-header .stake-text-wrapper {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}
.betslip-view .bet-header .backers-stake-text-wrapper,
.betslip-view .bet-header .stake-text-wrapper {
  width: 58px;
  padding: 4px 3px;
}
.betslip-view .bet-header .back-odds-text-wrapper,
.betslip-view .bet-header .backers-odds-text-wrapper,
.betslip-view .bet-header .odds-text-wrapper {
  width: 58px;
  padding: 4px 5px 4px 3px;
}
.betslip-view .bet-header .backers-odds-text-wrapper,
.betslip-view .bet-header .backers-stake-text-wrapper,
.betslip-view .bet-header .odds-text-wrapper {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}
.betslip-view .bet-header .options-wrapper .radio-liability-wrapper,
.betslip-view .bet-header .options-wrapper .radio-payout-wrapper {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  height: 14px;
  width: 66px;
}
.betslip-view .bet-header .options-wrapper .input-radio-liability,
.betslip-view .bet-header .options-wrapper .input-radio-payout {
  background-size: 10px;
  width: 11px;
  height: 10px;
  vertical-align: top;
  margin: 1px 1px 2px 2px;
}
.betslip-view .bet-header .backers-liability-text-wrapper,
.betslip-view .bet-header .options-wrapper,
.betslip-view .bet-header .profit-text-wrapper {
  padding: 4px 4px 4px 0;
  border: 0;
  text-align: center;
  vertical-align: middle;
  margin-bottom: 7px;
  display: table-cell;
  width: 66px;
}
.betslip-view .bet-header .backers-liability-text-wrapper.potential,
.betslip-view
  .bet-header
  .backers-liability-text-wrapper.potential
  .radio-liability-wrapper,
.betslip-view
  .bet-header
  .backers-liability-text-wrapper.potential
  .radio-payout-wrapper,
.betslip-view .bet-header .options-wrapper.potential,
.betslip-view .bet-header .options-wrapper.potential .radio-liability-wrapper,
.betslip-view .bet-header .options-wrapper.potential .radio-payout-wrapper,
.betslip-view .bet-header .profit-text-wrapper.potential,
.betslip-view
  .bet-header
  .profit-text-wrapper.potential
  .radio-liability-wrapper,
.betslip-view .bet-header .profit-text-wrapper.potential .radio-payout-wrapper {
  width: 53px;
}
.betslip-view
  .bet-header
  .backers-liability-text-wrapper.potential
  .potential-controller-radio,
.betslip-view
  .bet-header
  .options-wrapper.potential
  .potential-controller-radio,
.betslip-view
  .bet-header
  .profit-text-wrapper.potential
  .potential-controller-radio {
  cursor: pointer;
  color: #2789ce;
  width: 10px;
  height: 10px;
}
.betslip-view .bet-header .backers-liability-text-wrapper.potential-eachway,
.betslip-view
  .bet-header
  .backers-liability-text-wrapper.potential-eachway
  .radio-liability-wrapper,
.betslip-view
  .bet-header
  .backers-liability-text-wrapper.potential-eachway
  .radio-payout-wrapper,
.betslip-view .bet-header .options-wrapper.potential-eachway,
.betslip-view
  .bet-header
  .options-wrapper.potential-eachway
  .radio-liability-wrapper,
.betslip-view
  .bet-header
  .options-wrapper.potential-eachway
  .radio-payout-wrapper,
.betslip-view .bet-header .profit-text-wrapper.potential-eachway,
.betslip-view
  .bet-header
  .profit-text-wrapper.potential-eachway
  .radio-liability-wrapper,
.betslip-view
  .bet-header
  .profit-text-wrapper.potential-eachway
  .radio-payout-wrapper {
  width: 66px;
}
.betslip-view
  .bet-header
  .backers-liability-text-wrapper.potential-eachway
  .potential-controller-radio,
.betslip-view
  .bet-header
  .options-wrapper.potential-eachway
  .potential-controller-radio,
.betslip-view
  .bet-header
  .profit-text-wrapper.potential-eachway
  .potential-controller-radio {
  cursor: auto;
  width: 10px;
  height: 10px;
}
.betslip-view .bet-header .hint-wrapper {
  margin-right: 2px;
  width: 13px;
  height: 22px;
  display: table-cell;
  vertical-align: middle;
}
.betslip-view .bet-header .backers-odds-text {
  line-height: 10px;
  padding-bottom: 0;
  text-align: center;
  display: inline-block;
}
.betslip-view .bet-header .backers-stake-text {
  line-height: 10px;
  text-align: center;
  display: inline-block;
}
.betslip-view .bet-header .backers-liability-text {
  width: 55px;
  line-height: 10px;
  text-align: center;
  display: inline-block;
}
.betslip-view .hint-interrogation {
  cursor: help;
  color: #2789ce;
}
.betslip-view .market-name {
  background-color: #fff;
  height: 16px;
  line-height: 16px;
  white-space: pre-wrap;
  padding: 8px 8px 7px;
  text-align: left;
  font-weight: 700;
  font-size: 14px;
}
.betslip-view .empty {
  padding: 8px 8px 0;
}
.betslip-view .event-market-description {
  background-color: #fff;
  height: 24px;
  line-height: 20px;
  padding: 6px 8px 0;
  text-align: left;
  font-weight: 700;
  font-size: 14px;
  color: #1e1e1e;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.betslip-view .empty-betslip {
  text-align: center;
  padding: 0 68px;
}
.betslip-view .empty-betslip .event-market-description {
  border: 0;
  margin-top: 0;
  padding-top: 6px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.betslip-view .empty-betslip .sbw-multiples {
  border-radius: 2px;
  margin: 28px 0;
  min-height: 18px;
  padding: 4px 8px;
  line-height: 18px;
  text-align: center;
  text-decoration: none;
  font-size: 11px;
  display: inline-block;
  color: #1e1e1e;
  background: #ffb900;
}
.betslip-view .empty-betslip .sbw-multiples .sbw-multiples-bold {
  font-weight: 700;
}
.betslip-view .selection-text {
  background-color: #fff;
  height: auto;
  word-spacing: normal;
  padding: 0 8px;
  text-align: left;
  font-size: 11px;
}
.betslip-view .selection-text.highlighted {
  font-weight: 700;
  text-align: center;
  padding-top: 40px;
}
.betslip-view .selection-text.bottom {
  margin-top: 8px;
}
.betslip-view .selection-text .log-in {
  color: #2789ce;
  text-decoration: none;
  cursor: pointer;
}
.betslip-view .toRemove {
  width: 66px;
  display: table-cell;
}
.betslip-view .sp-bet-wrapper,
.betslip-view .unplaced-wrapper {
  font-size: 11px;
}
.betslip-view .sp-bet-wrapper .sp-bet-section,
.betslip-view .unplaced-wrapper .sp-bet-section {
  background-color: #303030;
  color: #fff;
  min-height: 28px;
}
.betslip-view .sp-bet-wrapper .sp-bet-section-top,
.betslip-view .unplaced-wrapper .sp-bet-section-top {
  padding-top: 6px;
}
.betslip-view .sp-bet-wrapper .sp-bet-section-top .sp-bet-starting-price,
.betslip-view .unplaced-wrapper .sp-bet-section-top .sp-bet-starting-price {
  font-weight: 700;
  float: left;
  padding-left: 8px;
  font-size: 12px;
}
.betslip-view .sp-bet-wrapper .sp-odds-limit-checkbox-wrapper,
.betslip-view .unplaced-wrapper .sp-odds-limit-checkbox-wrapper {
  float: right;
}
.betslip-view
  .sp-bet-wrapper
  .sp-odds-limit-checkbox-wrapper
  .sp-odds-limit-checkbox,
.betslip-view
  .unplaced-wrapper
  .sp-odds-limit-checkbox-wrapper
  .sp-odds-limit-checkbox {
  margin-right: 5px;
  float: left;
}
.betslip-view
  .sp-bet-wrapper
  .sp-odds-limit-checkbox-wrapper
  .sp-odds-limit-label,
.betslip-view
  .unplaced-wrapper
  .sp-odds-limit-checkbox-wrapper
  .sp-odds-limit-label {
  float: right;
  padding-left: 8px;
  padding-right: 6px;
  white-space: nowrap;
  width: 100px;
  height: 11px;
  text-overflow: ellipsis;
  overflow: hidden;
}
.betslip-view .sp-bet-wrapper .sp-bet-section-bottom,
.betslip-view .unplaced-wrapper .sp-bet-section-bottom {
  clear: both;
  padding: 6px 0 6px 8px;
}
.betslip-view .sp-bet-wrapper .has-not-sp-odds-limit.sp-lay.stake-text,
.betslip-view .unplaced-wrapper .has-not-sp-odds-limit.sp-lay.stake-text {
  line-height: 10px;
  padding-top: 4px;
  padding-bottom: 4px;
  width: 64px;
}
.betslip-view .sp-bet-wrapper .header-right-side-reconciliation,
.betslip-view .unplaced-wrapper .header-right-side-reconciliation {
  float: right;
}
.betslip-view .sp-bet-wrapper .header-right-side-reconciliation .odds-text,
.betslip-view .unplaced-wrapper .header-right-side-reconciliation .odds-text {
  width: 45px;
}
.betslip-view .sp-bet-wrapper .bet-price,
.betslip-view .sp-bet-wrapper .bet-profit,
.betslip-view .sp-bet-wrapper .bet-size,
.betslip-view .unplaced-wrapper .bet-price,
.betslip-view .unplaced-wrapper .bet-profit,
.betslip-view .unplaced-wrapper .bet-size {
  padding-top: 6px;
  padding-bottom: 6px;
  color: #1e1e1e;
}
.betslip-view .confirmation-container .bet-price {
  width: 56px;
  text-align: center;
  float: left;
  padding: 6px 4px 4px 3px;
  margin: 0;
}
.betslip-view .confirmation-container .bet-size.has-not-sp-odds-limit {
  margin-right: 70px;
}
.betslip-view .confirmation-container .bet-without-profit .bet-price {
  padding-right: 0;
}
.betslip-view .confirmation-container .bet-size {
  width: 60px;
  padding: 6px 3px 4px;
  float: left;
}
.betslip-view .confirmation-container .bet-profit {
  width: 56px;
}
.betslip-view .bet {
  min-height: 25px;
  border-bottom: 1px solid #fff;
  zoom: 1;
}
.betslip-view .bet::after {
  content: ".";
  display: block;
  clear: both;
  overflow: hidden;
  line-height: 0;
  height: 0;
}
.betslip-view .bet .bet-values {
  float: right;
}
.betslip-view .bet .oddsladder {
  margin-top: 2px;
}
.betslip-view .bet .stake-input-directive {
  margin-top: 3px;
  width: 56px;
  float: left;
}
.betslip-view .bet .readonly {
  color: #7e97a7;
}
.betslip-view .bet .bet-profit {
  display: inline-block;
  width: 56px;
  min-height: 12px;
  color: #273a47;
  text-align: center;
  padding: 6px 8px 6px 5px;
  white-space: pre-wrap;
}
.betslip-view .bet .bet-runner-name {
  display: block;
  float: left;
  font-weight: 700;
  color: #1e1e1e;
  text-align: left;
  padding: 7px 8px 6px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.betslip-view .bet .bet-runner-name.matched-bet {
  padding: 9px 8px 0;
}
.betslip-view .bet .close {
  vertical-align: top;
  width: 12px;
  height: 12px;
  border: 0;
  padding-bottom: 2px;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 0;
  padding-right: 0;
  cursor: pointer;
  float: left;
  margin: 6px 0 5px 8px;
}
.betslip-view .bet .active-for-removal,
.betslip-view .bet .close:active,
.betslip-view .bet .close:hover {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -13px;
}
.betslip-view .bet .has-not-sp-odds-limit {
  margin-right: 74px;
  padding-right: 0;
}
.betslip-view .bet.editable .bet-price,
.betslip-view .bet.editable .bet-size {
  padding: 6px 0 0;
  height: 26px;
  vertical-align: top;
}
.betslip-view .back-bets .bet {
  background-color: #dbefff;
}
.betslip-view .bet-report-messages {
  display: block;
  font-style: italic;
  padding-bottom: 6px;
  background-color: #dbefff;
  padding-left: 7px;
  font-size: 11px;
  color: #000;
  padding-top: 6px;
}
.betslip-view .bet-report-messages .receipt-message {
  display: block;
}
.betslip-view .bet-report-messages .receipt-error {
  display: block;
  color: #b30000;
  font-weight: 700;
  clear: both;
}
.betslip-view .bet-report-messages .deposit-link {
  padding-left: 6px;
  color: #2789ce;
  font-weight: 400;
  font-style: normal;
  text-decoration: none;
}
.betslip-view .lay-bets .bet,
.betslip-view .lay-bets .bet-report-messages {
  background-color: #fee9ee;
}
.betslip-view .footer-button-panel .betslip-cancel-btn {
  float: left;
  margin-left: 8px;
}
.betslip-view .betslip-footer {
  background-color: #efefef;
  overflow: auto;
}
.betslip-view .betslip-footer .liability {
  display: block;
  text-align: right;
  font-size: 12px;
  color: #273a47;
  padding: 6px 8px 7px;
}
.betslip-view .betslip-footer .liability .liability-value {
  font-weight: 700;
}
.betslip-view .betslip-footer .selection-panel-each-way {
  margin-top: 6px;
}
.betslip-view .betslip-footer .betslip-cancel-btn,
.betslip-view .betslip-footer .cancel-all-unmatched {
  float: left;
  margin-left: 8px;
  margin-bottom: 8px;
}
.betslip-view .betslip-footer .betslip-submit-btn,
.betslip-view .betslip-footer .view-open-bets {
  float: right;
}
.betslip-view .betslip-footer .checkboxes-area {
  clear: both;
  margin-bottom: 8px;
}
.betslip-view .betslip-footer .confirmation-panel {
  margin-top: 6px;
  margin-bottom: 40px;
}
.betslip-view .checkboxes-area .confirm-checkbox-wrapper,
.betslip-view .checkboxes-area .percentage-book-wrapper {
  margin: 8px 16px 8px 8px;
  text-align: left;
  color: #273a47;
  display: inline-block;
  line-height: 12px;
}
.betslip-view .checkboxes-area .confirm-checkbox,
.betslip-view .checkboxes-area .percentage-book-checkbox {
  margin-right: 5px;
  vertical-align: top;
  display: inline-block;
  float: left;
}
.betslip-view .countdown .loading-spinner {
  width: 28px;
  text-align: center;
  margin-left: calc(50% - 14px);
  margin-left: -webkit-calc(50% - 14px);
}
.betslip-view .countdown .placeholder {
  font-weight: 700;
  font-size: 11px;
  text-align: center;
  width: 400px;
  margin-top: 15px;
  margin-left: calc(50% - 200px);
  margin-left: -webkit-calc(50% - 200px);
}
.betslip-view .countdown .countdown-placeholder {
  font-weight: 700;
  font-size: 9px;
  text-align: center;
  width: 300px;
  margin-top: 10px;
  margin-left: calc(50% - 150px);
  margin-left: -webkit-calc(50% - 150px);
}
.betslip-view .countdown .counter {
  width: 9px;
  text-align: center;
  margin-left: calc(50% - 5px);
  margin-left: -webkit-calc(50% - 5px);
}
.betslip-view .loading {
  position: relative;
  min-height: 60px;
}
.betslip-view .loading .countdown {
  width: 100px;
  position: absolute;
  top: 65px;
  margin-left: calc(50% - 50px);
  margin-left: -webkit-calc(50% - 50px);
}
.betslip-view .contextual-help-modal-dialog .payout-liability-helper,
.betslip-view .contextual-help-modal-dialog .stake-helper {
  margin-bottom: 10px;
}
.betslip-view .bet.matched .bet-price,
.betslip-view .bet.matched .bet-profit,
.betslip-view .bet.matched .bet-size {
  margin-bottom: 6px;
  height: 10px;
  width: 58px;
}
.betslip-view .bet.receipt .bet-price,
.betslip-view .bet.receipt .bet-size {
  padding: 4px 2px;
}
.betslip-view .bet.receipt .bet-profit {
  width: 58px;
}
.betslip-view .receipt-container .sp.lay-bets-header .stake-text {
  height: 24px;
  padding-top: 4px;
  padding-bottom: 0;
  line-height: 10px;
}
.betslip-view .receipt-container .sp.lay-bets-header .odds-text {
  line-height: 10px;
}
.betslip-view .receipt-container .sp.lay-bets-header .lay-bet-text,
.betslip-view .receipt-container .sp.lay-bets-header .profit-text {
  line-height: 28px;
}
.betslip-view .receipt-container .current-bets-header-receipt {
  background-color: #303030;
  font-weight: 700;
  text-align: left;
  color: #fff;
  height: 19px;
  padding: 8px 8px 1px;
}
.betslip-view .receipt-container .current-bets-header-receipt.atinplay,
.betslip-view .receipt-container .current-bets-header-receipt.unplaced-bets {
  height: 37px;
}
.betslip-view .receipt-container .current-bets-header-receipt .header {
  font-weight: 700;
  font-size: 12px;
}
.betslip-view .receipt-container .current-bets-header-receipt .description {
  font-weight: 400;
  padding-top: 5px;
}
.betslip-view .receipt-container .unplaced-wrapper .bet-header {
  border-top: 1px solid #fff;
}
.betslip-view .receipt-container .bet.receipt .bet-price {
  width: 56px;
}
.betslip-view .matched-wrapper .current-bets-header-receipt {
  height: 20px;
}
.betslip-view .matched-wrapper .average-odd-wrapper {
  height: 25px;
  width: 100%;
  border-top: 1px solid #fff;
}
.betslip-view .matched-wrapper .back-average-odd-wrapper {
  height: 25px;
  width: 100%;
  border-top: 1px solid #fff;
  background-color: #dbefff;
}
.betslip-view .matched-wrapper .lay-average-odd-wrapper {
  height: 25px;
  width: 100%;
  border-top: 1px solid #fff;
  background-color: #fee9ee;
}
.betslip-view .matched-wrapper .average-odd {
  color: #273a47;
  width: 55px;
  padding-top: 7px;
  float: right;
  margin-right: 81px;
  text-align: center;
  font-weight: 700;
}
.betslip-view .matched-wrapper .asian-handicap .average-odd {
  margin-right: 0;
}
.betslip-view .bet.unplaced {
  padding-bottom: 4px;
  height: 100%;
}
.betslip-view .bet.no-error {
  height: 100%;
  padding-bottom: 6px;
}
.betslip-view .receipt .bet-ref {
  clear: both;
  margin-left: 8px;
  color: #999;
}
.betslip-view .receipt-text {
  background-color: #fff;
  height: 15px;
  line-height: 15px;
  white-space: pre-wrap;
  padding: 8px 8px 7px;
  text-align: left;
  font-weight: 700;
  font-size: 14px;
  color: #1e1e1e;
}
.betslip-view .betslip-footer.receipt {
  padding: 8px 0;
}
.betslip-view .betslip-footer.receipt .betslip-cancel-btn,
.betslip-view .betslip-footer.receipt .betslip-submit-btn {
  margin-bottom: 0;
  white-space: nowrap;
  max-width: 50%;
  overflow: hidden;
  text-overflow: ellipsis;
}
.betslip-view .betslip-header {
  height: 30px;
  zoom: 1;
}
.betslip-view .betslip-header::after {
  content: ".";
  display: block;
  clear: both;
  overflow: hidden;
  line-height: 0;
  height: 0;
}
.betslip-view .betslip-header .markets {
  float: left;
}
.betslip-view .open-container .sp .oddsladder {
  margin-right: 7px;
}
.betslip-view .open-container .markets {
  float: left;
}
.betslip-view .open-container .order-bet-header {
  clear: both;
  min-height: 22px;
  overflow: auto;
  text-align: center;
  height: 30px;
  width: 100%;
  display: table;
}
.betslip-view .open-container .order-bet-header .order-bet-wrapper {
  display: table-row;
}
.betslip-view .open-container .order-bet-header .bet-text-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.betslip-view .open-container .order-bet-header .bet-text-wrapper .bet-text {
  text-align: left;
  padding: 0 2px 0 8px;
  white-space: pre-wrap;
}
.betslip-view .open-container .order-bet-header .odds-text-wrapper,
.betslip-view .open-container .order-bet-header .stake-text-wrapper {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
  width: 58px;
}
.betslip-view .open-container .order-bet-header .stake-text-wrapper {
  padding: 4px 3px;
}
.betslip-view .open-container .order-bet-header .odds-text-wrapper {
  padding: 4px 2px 4px 3px;
}
.betslip-view .open-container .order-bet-header .profit-text-wrapper {
  padding: 4px 0 4px 3px;
  border: 0;
  text-align: center;
  vertical-align: middle;
  margin-bottom: 7px;
  display: table-cell;
  width: 66px;
}
.betslip-view
  .open-container
  .order-bet-header
  .profit-text-wrapper
  .profit-text {
  white-space: pre-wrap;
}
.betslip-view .open-container .lay-bets-header .header-right-side {
  height: 28px;
}
.betslip-view .open-container .sp-bet-wrapper .lay-bets-header {
  overflow: hidden;
}
.betslip-view .open-container .sp-bet-wrapper .lay-bets-header .odds-text {
  vertical-align: top;
  line-height: 10px;
}
.betslip-view .open-container .sp-bet-wrapper .lay-bets-header .stake-text {
  height: 28px;
  line-height: 10px;
  margin-top: 4px;
}
.betslip-view .open-container .sp-bet-wrapper .lay-bets-header .profit-text {
  height: 28px;
  line-height: 10px;
  vertical-align: top;
}
.betslip-view .confirmation-container .bet-without-profit .bet-size,
.betslip-view .open-container .bet-without-profit .bet-size,
.betslip-view .receipt-container .bet-without-profit .bet-size {
  text-align: right;
  padding: 6px 8px 6px 5px;
}
.betslip-view .open-selection-text {
  margin-top: 40px;
}
.betslip-view .open-selection-text .selection-text {
  background-color: #fff;
  padding: 0 8px 4px;
  text-align: center;
  font-size: 11px;
  font-weight: 700;
}
.betslip-view .open-selection-text .selection-text.unmatched {
  text-align: left;
}
.betslip-view .current-bets-header-open.matched {
  overflow: hidden;
  height: 1%;
  padding-bottom: 5px;
}
.betslip-view .current-bets-header-open.matched .matched-text {
  float: left;
  font-size: 12px;
}
.betslip-view .current-bets-header-open.matched .order-date-checkbox-wrapper {
  float: right;
  font-weight: 400;
  width: 50%;
  text-align: right;
}
.betslip-view .current-bets-header-open.matched .order-date-checkbox {
  margin-right: 3px;
  vertical-align: top;
}
.betslip-view .open-footer {
  clear: both;
  background-color: #efefef;
}
.betslip-view .open-footer .footer-bet-info-checkbox-wrapper {
  clear: both;
  padding: 8px;
  margin-top: 8px;
  line-height: 12px;
}
.betslip-view .open-footer .checkboxes-area {
  clear: both;
  padding: 0 8px 8px;
}
.betslip-view .checkboxes-area .average-odd-checkbox-wrapper,
.betslip-view .checkboxes-area .consolidate-checkbox-wrapper,
.betslip-view .checkboxes-area .matched-bets-checkbox-wrapper {
  display: inline-block;
  margin-right: 10px;
  line-height: 12px;
}
.betslip-view .checkboxes-area .average-odd-checkbox,
.betslip-view .checkboxes-area .consolidate-checkbox,
.betslip-view .checkboxes-area .matched-bets-checkbox,
.betslip-view .open-footer .footer-bet-info-checkbox {
  vertical-align: top;
  margin-right: 3px;
}
.betslip-view .open-footer .footer-button-panel {
  padding-top: 8px;
}
.betslip-view .footer-button-panel .right {
  float: right;
  margin-left: 0;
}
.betslip-view .refresh-button {
  border: 0;
  background-color: #303030;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  color: #fff;
  padding: 0 10px;
  cursor: pointer;
  font-size: 11px;
  line-height: 16px;
  float: right;
  margin: 7px 4px 5px;
}
.betslip-view .refresh-button:active {
  background-color: #000;
  color: #7e97a7;
}
.betslip-view .refresh-button:focus {
  outline: 0;
}
.betslip-view .refresh-button:hover {
  cursor: pointer;
}
.betslip-view .current-bets-header,
.betslip-view .current-bets-header-open {
  background-color: #303030;
  font-size: 12px;
  height: 20px;
  font-weight: 700;
  text-align: left;
  color: #fff;
  padding: 8px 8px 1px;
  display: block;
}
.betslip-view .has-changed {
  font-weight: 700;
}
.betslip-view .has-changed-red {
  font-weight: 700;
  color: #b30000;
}
.betslip-view .bet-at-in-play-wrapper {
  height: 7px;
}
.betslip-view .bet-at-in-play-wrapper .at-in-play-text {
  float: left;
  line-height: 12px;
}
.betslip-view .bet-at-in-play-wrapper .radio-btn-cancel-wrapper,
.betslip-view .bet-at-in-play-wrapper .radio-btn-keep-wrapper,
.betslip-view .bet-at-in-play-wrapper .radio-btn-take-sp-wrapper {
  float: left;
  margin-left: 10px;
  font-weight: 400;
  line-height: 12px;
}
.betslip-view
  .bet-at-in-play-wrapper
  .radio-btn-cancel-wrapper
  .radio-btn-cancel,
.betslip-view .bet-at-in-play-wrapper .radio-btn-keep-wrapper .radio-btn-keep,
.betslip-view
  .bet-at-in-play-wrapper
  .radio-btn-take-sp-wrapper
  .radio-btn-take-sp {
  vertical-align: top;
}
.betslip-view .bet.atinplay .bet-at-in-play-wrapper {
  clear: both;
  padding: 6px 0 5px 8px;
  font-weight: 700;
  text-align: left;
}
.betslip-view .bet-matching-info {
  clear: both;
  font-size: 10px;
}
.betslip-view .bet.open .bet-matching-info,
.betslip-view .cancelled-wrapper .bet.receipt .bet-matching-info {
  padding-top: 2px;
}
.betslip-view .bet.open .bet-ref {
  float: left;
  margin-top: 2px;
  margin-left: 8px;
  color: #999;
}
.betslip-view .bet.open .bet-runner-name,
.betslip-view .bet.open .close {
  margin-bottom: 0;
}
.betslip-view .bet.open .bet-runner-name {
  padding-top: 7px;
}
.betslip-view .bet-matching-info .bet-matched-date,
.betslip-view .bet-matching-info .bet-submitted-date {
  display: inline-block;
  margin-left: 8px;
  margin-top: 2px;
  color: #999;
}
.betslip-view .bet.open {
  padding-bottom: 6px;
}
.betslip-view .bet.open .bet-values {
  height: 20px;
  padding-top: 3px;
}
.betslip-view .bet.open.is-each-way .bet-values {
  padding-top: 0;
}
.betslip-view .bet.editable {
  height: 56px;
}
.betslip-view .bet.atinplay {
  padding-bottom: 6px;
}
.betslip-view .errors-wrapper .error-statement {
  font-weight: 700;
  font-size: 11px;
  color: #b30000;
  margin-left: 8px;
  margin-bottom: 8px;
}
.betslip-view .errors-wrapper .error-statement:first-child {
  margin-top: 0;
}
.betslip-view .loading-wrapper {
  font-weight: 700;
  width: 100%;
  text-align: center;
  position: relative;
}
.betslip-view .loading-wrapper .loading-text {
  display: block;
  padding-top: 55px;
  font-weight: 700;
  font-size: 14px;
  color: #273a47;
}
.betslip-view .betslip-pnl {
  clear: both;
  overflow: auto;
  margin-bottom: 4px;
}
.betslip-view .betslip-pnl .betslip-pnl-row {
  padding: 0 8px;
  clear: both;
}
.betslip-view .betslip-pnl .betslip-pnl-row .betslip-pnl-label {
  float: left;
  font-size: 11px;
  color: #000;
  line-height: 15px;
}
.betslip-view .betslip-pnl .betslip-pnl-row .betslip-pnl-value {
  float: right;
  font-size: 11px;
  color: #b30000;
  line-height: 15px;
}
.betslip-view .betslip-pnl .betslip-pnl-row .betslip-pnl-value.positive {
  color: #1c6700;
}
.betslip-view .betslip-pnl.unmatched-view {
  padding-top: 3px;
}
.betslip-view .betslip-pnl.potentials-view .betslip-pnl-label,
.betslip-view .betslip-pnl.unmatched-view .betslip-pnl-label {
  margin-left: 20px;
}
input.invalid {
  border: 1px solid #b30000 !important;
}
.betslip-dialog .dialog-body {
  padding: 16px;
  border-bottom: 1px solid #dfdfdf;
  font: 12px Arial, Helvetica, sans-serif;
}
.betslip-dialog .dialog-body .message {
  text-align: justify;
  color: #303030;
}
.betslip-dialog .dialog-footer {
  padding: 0 16px;
}
.betslip-dialog .dialog-footer .primary-action {
  width: 96px;
  height: 24px;
  float: right;
  margin: 16px 0;
}
.oddsladder .odds-input,
.oddsladder .price-input {
  text-align: center;
  width: 40px;
  height: 13px;
  padding: 2px 0;
  border: 1px solid #ccc;
  line-height: normal;
}
.oddsladder .readonly {
  color: #7e97a7;
}
.oddsladder .odds-ladder-left,
.oddsladder .odds-ladder-right {
  float: left;
  height: 19px;
  padding: 1px 0;
}
.oddsladder .odds-ladder-right .button-separator {
  width: 13px;
  height: 1px;
  background-color: #ccc;
}
.oddsladder .odds-ladder-right .arrow-btn {
  cursor: pointer;
  display: block;
  width: 13px;
  height: 9px;
  margin: 0;
  padding: 0;
  border: 1px solid #ccc;
  background-color: #eee;
}
.oddsladder .odds-ladder-right .arrow-btn::-moz-focus-inner {
  padding: 0;
  border: 0 none;
}
.oddsladder .odds-ladder-right .arrow-btn:disabled {
  -moz-opacity: 0.5;
  -khtml-opacity: 0.5;
  -webkit-opacity: 0.5;
  opacity: 0.5;
}
.oddsladder .odds-ladder-right .arrow-btn .arrow-down {
  height: 7px;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 2px -151px;
}
.oddsladder .odds-ladder-right .arrow-btn .arrow-up {
  height: 7px;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 2px -146px;
}
.oddsladder .ng-invalid {
  border: 1px solid #c00;
}
.max-payout-liability {
  background: #fff9d8;
  padding: 7px 8px 8px;
  position: absolute;
  z-index: 10;
  border: 1px solid #7d97a8;
  display: none;
}
.max-payout-liability.visible {
  display: block;
}
.max-payout-liability .max-payout-liability-info {
  color: #273a47;
  font-weight: 700;
  margin-bottom: 3px;
  font-size: 11px;
  padding: 0;
}
.max-payout-liability .max-payout-liability-container {
  overflow: auto;
  clear: both;
}
.max-payout-liability .max-payout-liability-label {
  float: left;
  line-height: 17px;
}
.max-payout-liability .max-payout-liability-label .currency-code {
  float: left;
}
.max-payout-liability .max-payout-liability-btn {
  font-weight: 700;
  font-size: 11px;
  text-align: center;
  line-height: 16px;
  height: 18px;
  padding: 0 10px;
  background-color: #cbcbcb;
  border: 0;
  border-bottom: 1px solid #94a8b3;
  float: left;
  margin: 0;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
}
.max-payout-liability .max-payout-liability-btn:focus {
  box-shadow: inset 0 2px 5px 2px rgba(0, 0, 0, 0.2);
  border: 0;
}
.max-payout-liability .max-payout-liability-input {
  width: 50px;
  height: 16px;
  border: 1px solid #e0e6e6;
  text-align: center;
  font-size: 11px;
  font-weight: 400;
  color: #273a47;
  float: left;
  margin-right: 4px;
  margin-left: 8px;
}
.max-payout-liability .max-payout-liability-input:focus {
  border: 1px solid #3b5160;
}
.popup-overlay {
  width: 100%;
  height: 100%;
  z-index: 9;
  position: absolute;
  top: 0;
  left: 0;
  background-color: #fff;
  opacity: 0;
}
.loading-spinner {
  width: 28px;
  height: 28px;
  background-image: url(images/app/common/assets/images/betslip_spinner_4627_.gif);
  background-repeat: no-repeat;
  background-position: top left;
  background-color: transparent;
}
.stake-input-directive {
  display: inline-block;
  text-align: center;
  vertical-align: top;
  width: 50px;
  height: 21px;
  padding-right: 4px;
}
.bet .size-input {
  display: inline-block;
  color: #273a47;
  text-align: center;
  vertical-align: top;
  width: 50px;
  height: 13px;
  padding: 2px 0;
  border: 1px solid #ccc;
}
.tabs .tab-content {
  float: left;
  width: 100%;
}
.tabs .pane,
.tabs .subpane {
  display: none;
}
.tabs .pane.active,
.tabs .subpane.active {
  display: block;
}
.tabs .generic-tabs-container .generic-tab#betslip-tab-xsell {
  float: right;
}
.tabs .generic-tabs-container .generic-tab .tab-title {
  line-height: 26px;
}
.tabs .generic-tabs-container .generic-tab .nav-tab-special {
  border-right: 0;
}
.tabs
  .generic-tabs-container
  .generic-tab
  .nav-tab-special.generic-tab-not-selected {
  border-left: 1px solid #dfdfdf;
}
.tabs
  .generic-tabs-container
  .generic-tab
  .nav-tab-special.generic-tab-selected {
  padding-right: 16px;
}
.nav-modal-dialog {
  color: #444;
}
.nav-modal-dialog .dialog-msg {
  font-weight: 700;
}
.nav-modal-dialog .dialog-buttons {
  text-align: center;
}
.nav-modal-dialog .dialog-button {
  cursor: pointer;
  color: #444;
  font-weight: 700;
  border-radius: 4px;
  border-width: 1px;
  border-color: #eee #eee #bbb;
  padding: 4px 6px;
  background: linear-gradient(0deg, #fff, #eaeff2);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#eaeff2", endColorstr="white", GradientType=0);
}
.nav-modal-dialog .dialog-button:first-child {
  margin-right: 20px;
}
.nav-modal-dialog .show-again-msg {
  position: absolute;
  bottom: 10px;
  left: 10px;
}
.nav-modal-dialog .show-again-msg .show-again-option {
  margin-right: 4px;
}
.favourites-notifications-container .message-holder {
  position: absolute;
  left: 3px;
  top: -6px;
  z-index: 1;
  border: 1px solid #e3e8e8;
  background-color: #fff;
  box-shadow: 0 1px 8px 0 rgba(0, 0, 0, 0.3);
  line-height: 22px;
  height: 22px;
  color: #1e1e1e;
  opacity: 0;
  -webkit-opacity: 0;
  -moz-opacity: 0;
  visibility: collapse;
}
.favourites-notifications-container .message-holder::after,
.favourites-notifications-container .message-holder::before {
  top: 100%;
  left: 30px;
  border: solid transparent;
  content: " ";
  height: 0;
  width: 0;
  position: absolute;
  pointer-events: none;
}
.favourites-notifications-container .message-holder::after {
  border-color: rgba(255, 255, 255, 0);
  border-top-color: #fff;
  border-width: 6px;
}
.favourites-notifications-container .message-holder::before {
  border-color: rgba(255, 255, 255, 0);
  border-top-color: #fff;
  border-width: 7px;
}
.favourites-notifications-container .message-holder.show {
  visibility: visible;
  opacity: 1;
  -webkit-opacity: 1;
  -moz-opacity: 1;
  transition: all 1s ease;
  -moz-transition: all 1s ease;
  -webkit-transition: all 1s ease;
}
.favourites-notifications-container .message-holder.fadeOut {
  transition: all 1s ease;
  -moz-transition: all 1s ease;
  -webkit-transition: all 1s ease;
}
.favourites-notifications-container .message-holder .icon {
  display: block;
  margin: 4px 4px 0;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -687px;
  width: 12px;
  height: 12px;
  float: left;
}
.favourites-notifications-container .message-holder .status {
  float: left;
  display: block;
  margin-right: 4px;
  font-weight: 700;
}
.favourites-notifications-container .message-holder .message {
  float: left;
  display: block;
  padding-right: 8px;
}
.is-collapsed .favourites-notifications-container .message-holder {
  left: 8px;
  top: 6px;
}
.is-collapsed .favourites-notifications-container .message-holder::after,
.is-collapsed .favourites-notifications-container .message-holder::before {
  left: 2px;
}
.fake-games-widget {
  width: 243px;
  height: 254px;
  background-color: #fff;
}
.fake-games-header {
  width: 100%;
  height: 28px;
  background-color: #acacac;
}
.fake-games-content {
  width: 100%;
  height: 198px;
  position: relative;
  background-color: #ebebeb;
}
.fake-games-content::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  border-left: 1px solid #fff;
}
.fake-games-content-game {
  width: 100%;
  height: 64px;
  position: absolute;
  margin-top: 64px;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #fff;
}
.mod-head2head .mod-head2head-tennis {
  padding-top: 8px;
}
.mod-head2head .mod-head2head-tennis .players {
  width: 100%;
  display: table;
}
.mod-head2head .mod-head2head-tennis .players .column {
  display: table-cell;
  vertical-align: top;
}
.mod-head2head .mod-head2head-tennis .players .column-attributes {
  padding: 0 12px;
}
.mod-head2head .mod-head2head-tennis .players .player-image {
  width: 120px;
  height: 150px;
}
.mod-head2head .mod-head2head-tennis .players .attributes {
  width: 100%;
  table-layout: fixed;
}
.mod-head2head .mod-head2head-tennis .players .attributes td {
  padding-bottom: 14px;
  text-overflow: ellipsis;
  overflow: hidden;
}
.mod-head2head .mod-head2head-tennis .players .attributes .player-name {
  font-weight: 700;
}
.mod-head2head .mod-head2head-tennis .players .attributes .middle {
  width: 90px;
  text-align: center;
  font-weight: 700;
  padding-left: 32px;
  padding-right: 32px;
}
.mod-head2head .mod-head2head-tennis .tennis-recent-matches .match-wrapper {
  margin-top: 15px;
  position: relative;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .section-title {
  text-align: left;
  padding-left: 8px;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .filter {
  position: absolute;
  right: 8px;
  top: 3px;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info-wrapper {
  padding: 0 8px;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info {
  width: 100%;
  table-layout: fixed;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell {
  line-height: 16px;
  padding-right: 8px;
  height: 25px;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-header
  .match-cell {
  font-weight: 700;
  height: 30px;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-body
  .match-row {
  border-bottom: 1px solid #ececec;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-body
  .match-row:last-child {
  border-bottom: 0;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.date,
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.round,
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.surface {
  width: 15%;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.results {
  width: 15%;
  display: none;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.opponent,
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.tournament {
  width: 20%;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.results-and-sets {
  width: 15%;
  white-space: normal;
  overflow: visible;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.results-and-sets
  .set::after {
  content: "|";
  padding: 0 5px;
}
.mod-head2head
  .mod-head2head-tennis
  .tennis-recent-matches
  .match-wrapper
  .matches-info
  .match-cell.results-and-sets
  .set:last-child::after {
  content: "";
}
@media only screen and (max-width: 1279px) {
  .mod-head2head .mod-head2head-tennis .players .player-image {
    width: 80px;
    height: 100px;
  }
  .mod-head2head .mod-head2head-tennis .players .attributes .middle {
    padding-left: 16px;
    padding-right: 16px;
  }
  .mod-head2head
    .mod-head2head-tennis
    .tennis-recent-matches
    .match-wrapper
    .matches-info
    .match-cell.results-and-sets {
    display: none;
  }
  .mod-head2head
    .mod-head2head-tennis
    .tennis-recent-matches
    .match-wrapper
    .matches-info
    .match-cell.results {
    display: table-cell;
  }
}
@media only screen and (max-width: 1024px) {
  .mod-head2head .mod-head2head-tennis .players .attributes .middle {
    padding-left: 8px;
    padding-right: 8px;
  }
}
.mod-head2head {
  padding-top: 8px;
}
.mod-head2head .not-available {
  padding: 10px 0;
  padding-top: 5px;
  font-size: 12px;
  text-align: center;
}
.mod-head2head .section-title {
  height: 25px;
  line-height: 25px;
  background-color: #ececec;
  font-weight: 700;
  text-align: center;
}
.mod-head2head .align-left {
  text-align: left;
}
.mod-head2head .align-right {
  text-align: right;
}
.mod-head2head .top-scorers .teams-scorers {
  vertical-align: top;
  width: 50%;
  display: inline-block;
  text-align: center;
  -khtml-box-sizing: border-box;
  box-sizing: border-box;
}
.mod-head2head .top-scorers .teams-scorers .no-scorers-info {
  margin: 10px 0;
}
.mod-head2head .top-scorers .teams-scorers .scorers {
  margin: 5px 0;
}
.mod-head2head .top-scorers .teams-scorers .scorers .player {
  display: table;
  line-height: 22px;
  width: 150px;
}
.mod-head2head .top-scorers .teams-scorers .scorers .player .name {
  display: table-cell;
  text-align: left;
}
.mod-head2head .top-scorers .teams-scorers .scorers .player .goals {
  display: table-cell;
  text-align: right;
  vertical-align: middle;
}
.mod-head2head .top-scorers .home-team {
  padding-right: 1px;
}
.mod-head2head .top-scorers .away-team {
  padding-left: 1px;
}
.mod-head2head .league-positions .positions {
  table-layout: fixed;
  margin: 12px auto;
}
.mod-head2head .league-positions .positions th {
  font-weight: 700;
  width: 40px;
}
.mod-head2head .league-positions .positions td {
  padding-top: 10px;
  width: 40px;
}
.mod-head2head .league-positions .positions .position {
  width: 54px;
  padding-right: 8px;
}
.mod-head2head .league-positions .positions .team {
  width: 160px;
  padding-right: 8px;
}
.mod-head2head .league-positions .positions .draw,
.mod-head2head .league-positions .positions .loss,
.mod-head2head .league-positions .positions .played,
.mod-head2head .league-positions .positions .points,
.mod-head2head .league-positions .positions .win {
  text-align: center;
}
.mod-head2head .teams-line-up .teams-line-up-body {
  overflow: hidden;
  max-height: 350px;
  transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -webkit-transition: all 0.3s ease-in-out;
}
.mod-head2head .teams-line-up .teams-line-up-body.hide {
  max-height: 0;
}
.mod-head2head .teams-line-up .teams-line-up-footer {
  border-top: 1px solid #dedede;
  text-align: center;
  padding: 10px;
  margin-top: 4px;
}
.mod-head2head .teams-line-up .line-up-button {
  border: 0;
  background: linear-gradient(0deg, #c2c2c2, #dedede);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#dedede", endColorstr="#c2c2c2", GradientType=0);
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  padding: 0 8px;
  margin: 0;
  cursor: pointer;
  font-size: 11px;
  color: #1e1e1e;
  line-height: 16px;
}
.mod-head2head .teams-line-up .line-up-button:active {
  color: #7e97a7;
}
.mod-head2head .teams-line-up .line-up-button:focus {
  outline: 0;
}
.mod-head2head .teams-line-up .line-up-button:hover {
  cursor: pointer;
}
.mod-head2head .teams-line-up .teams {
  display: inline-block;
  width: 50%;
  vertical-align: top;
  margin: 6px 0;
}
.mod-head2head .teams-line-up .teams .team-name {
  font-size: 20px;
  text-align: center;
}
.mod-head2head .teams-line-up .teams .line-up-no-info {
  text-align: center;
  margin-top: 4px;
}
.mod-head2head .teams-line-up .teams .line-up-info {
  margin-top: 4px;
}
.mod-head2head .teams-line-up .teams .line-up-info .filters {
  text-align: center;
  table-layout: fixed;
  display: table;
  width: 100%;
}
.mod-head2head .teams-line-up .teams .line-up-info .filters .starting-team {
  display: table-cell;
  text-align: right;
}
.mod-head2head
  .teams-line-up
  .teams
  .line-up-info
  .filters
  .starting-team:hover {
  cursor: pointer;
  text-decoration: underline;
}
.mod-head2head
  .teams-line-up
  .teams
  .line-up-info
  .filters
  .starting-team.selected {
  font-weight: 700;
  cursor: default;
  text-decoration: none;
}
.mod-head2head .teams-line-up .teams .line-up-info .filters .subs {
  display: table-cell;
  text-align: left;
}
.mod-head2head .teams-line-up .teams .line-up-info .filters .subs:hover {
  cursor: pointer;
  text-decoration: underline;
}
.mod-head2head .teams-line-up .teams .line-up-info .filters .subs.selected {
  font-weight: 700;
  cursor: default;
  text-decoration: none;
}
.mod-head2head .teams-line-up .teams .line-up-info .filters .separator {
  display: table-cell;
  width: 16px;
}
.mod-head2head .teams-line-up .teams .line-up-info .starting-line-up,
.mod-head2head .teams-line-up .teams .line-up-info .subs-line-up {
  margin: 10px 10px 0;
  display: none;
}
.mod-head2head .teams-line-up .teams .line-up-info .starting-line-up.visible,
.mod-head2head .teams-line-up .teams .line-up-info .subs-line-up.visible {
  display: block;
}
.mod-head2head .teams-line-up .teams .line-up-info .starting-line-up .player,
.mod-head2head .teams-line-up .teams .line-up-info .subs-line-up .player {
  line-height: 20px;
  display: table;
  margin-bottom: 1px;
  width: 200px;
  text-align: left;
  border-spacing: 1px 0;
  color: #1e1e1e;
}
.mod-head2head
  .teams-line-up
  .teams
  .line-up-info
  .starting-line-up
  .player
  .position,
.mod-head2head
  .teams-line-up
  .teams
  .line-up-info
  .subs-line-up
  .player
  .position {
  background-color: #ececec;
  display: table-cell;
  font-weight: 700;
  width: 20px;
  text-align: center;
  vertical-align: middle;
  font-size: 10px;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
}
.mod-head2head
  .teams-line-up
  .teams
  .line-up-info
  .starting-line-up
  .player
  .number,
.mod-head2head
  .teams-line-up
  .teams
  .line-up-info
  .subs-line-up
  .player
  .number {
  border: 1px solid #ececec;
  padding: 0;
  display: table-cell;
  width: 20px;
  text-align: center;
  vertical-align: middle;
  font-size: 10px;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
}
.mod-head2head
  .teams-line-up
  .teams
  .line-up-info
  .starting-line-up
  .player
  .name,
.mod-head2head .teams-line-up .teams .line-up-info .subs-line-up .player .name {
  display: table-cell;
  padding-left: 8px;
  line-height: 14px;
  vertical-align: middle;
}
.mod-head2head .recent-matches .team-matches {
  width: 50%;
  display: inline-block;
  text-align: center;
  vertical-align: top;
  -khtml-box-sizing: border-box;
  box-sizing: border-box;
}
.mod-head2head .recent-matches .team-matches.home-team {
  padding-right: 1px;
}
.mod-head2head .recent-matches .team-matches.away-team {
  padding-left: 1px;
}
.mod-head2head .recent-matches .filter {
  width: 100%;
  display: table;
  table-layout: fixed;
  margin: 12px 0;
}
.mod-head2head .recent-matches .filter-option {
  display: table-cell;
}
.mod-head2head .recent-matches .filter-option:hover {
  cursor: pointer;
  text-decoration: underline;
}
.mod-head2head .recent-matches .filter-option.selected {
  font-weight: 700;
  cursor: default;
  text-decoration: none;
}
.mod-head2head .recent-matches .filter-separator {
  width: 16px;
  display: table-cell;
}
.mod-head2head .recent-matches .results {
  margin-bottom: 10px;
}
.mod-head2head .recent-matches .results .short {
  display: block;
}
.mod-head2head .recent-matches .results .short > .result {
  display: inline-block;
  width: 21px;
  height: 20px;
  font-weight: 700;
  margin-left: 2px;
  border-radius: 2px;
  color: #fff;
  font-size: 12px;
  line-height: 20px;
}
.mod-head2head .recent-matches .results .short > .result:first-child {
  margin-left: 0;
}
.mod-head2head .recent-matches .results .short > .result.win {
  background-color: #090;
}
.mod-head2head .recent-matches .results .short > .result.draw {
  background-color: #a8a8a8;
}
.mod-head2head .recent-matches .results .short > .result.loss {
  background-color: #f33;
}
.mod-head2head .recent-matches .results .full {
  margin: 12px 0;
}
.mod-head2head .recent-matches .results .full li {
  display: table;
  table-layout: fixed;
  width: 100%;
  margin-top: 10px;
}
.mod-head2head .recent-matches .results .full li:first-child {
  margin-top: 0;
}
.mod-head2head .recent-matches .results .full .score {
  display: table-cell;
  width: 56px;
}
.mod-head2head .recent-matches .results .full .team {
  display: table-cell;
}
.mod-head2head .recent-matches .winner-A .team-a,
.mod-head2head .recent-matches .winner-H .team-h {
  font-weight: 700;
}
.mod-head2head .match-preview .match-preview-team {
  vertical-align: top;
  width: 50%;
  display: inline-block;
  text-align: left;
  -khtml-box-sizing: border-box;
  box-sizing: border-box;
  padding: 12px 8px;
}
.mod-head2head .match-preview .home-team {
  padding-right: 9px;
}
.mod-head2head .match-preview .away-team {
  padding-left: 9px;
}
.mod-head2head .recent-meetings .recent-meetings-container {
  margin: 10px 0;
}
.mod-head2head .recent-meetings .recent-meetings-container .meeting {
  line-height: 20px;
}
.mod-head2head .recent-meetings .recent-meetings-container .meeting .left-cell {
  width: 45%;
  display: inline-block;
  text-align: right;
}
.mod-head2head
  .recent-meetings
  .recent-meetings-container
  .meeting
  .left-cell
  .date {
  display: inline-block;
}
.mod-head2head
  .recent-meetings
  .recent-meetings-container
  .meeting
  .left-cell
  .home-team {
  width: 53%;
  display: inline-block;
}
.mod-head2head
  .recent-meetings
  .recent-meetings-container
  .meeting
  .left-cell
  .home-team.winner {
  font-weight: 700;
}
.mod-head2head
  .recent-meetings
  .recent-meetings-container
  .meeting
  .middle-cell {
  width: 10%;
  display: inline-block;
  text-align: center;
}
.mod-head2head
  .recent-meetings
  .recent-meetings-container
  .meeting
  .middle-cell
  .result
  .winner {
  font-weight: 700;
}
.mod-head2head
  .recent-meetings
  .recent-meetings-container
  .meeting
  .right-cell {
  display: inline-block;
}
.mod-head2head
  .recent-meetings
  .recent-meetings-container
  .meeting
  .right-cell
  .away-team.winner {
  font-weight: 700;
}
.head2head-modal-dialog .head2head-modal-title {
  font-size: 14px;
  color: #1e1e1e;
  font-weight: 700;
  background: #dfdfdf;
  margin-top: -16px;
  margin-right: -16px;
  padding: 0 16px;
  height: 32px;
  line-height: 32px;
  border-bottom-width: 0;
}
.head2head-modal-dialog .head2head-modal-content-wrapper {
  height: 520px;
  overflow-y: auto;
}
.head2head-modal-dialog .head2head-modal-content {
  height: 100%;
  padding: 0 16px;
}
.head2head-modal-dialog .head2head-modal-content::before {
  content: " ";
  width: calc(100% - 16px);
  height: 3em;
  position: absolute;
  bottom: 0;
  left: 0;
  background: linear-gradient(to top, #fffcfc, rgba(255, 252, 252, 0));
  z-index: 1;
}
.head2head-modal-dialog .mod-head2head {
  padding-bottom: 16px;
}
.mod-inline-betting .loading-panel .progress-bar-container .progress-bar {
  transition: width 1s linear;
  -moz-transition: width 1s linear;
  -webkit-transition: width 1s linear;
}
.mod-inline-betting .notification-panel-animate.ng-leave {
  transition: all 0.25s linear;
  -moz-transition: all 0.25s linear;
  -webkit-transition: all 0.25s linear;
  opacity: 1;
}
.mod-inline-betting .notification-panel-animate.ng-leave.ng-leave-active {
  opacity: 0;
}
.mod-inline-betting * {
  line-height: inherit;
}
.mod-inline-betting.narrow .place-bet-panel.extra-small .bet-info {
  display: none;
}
.mod-inline-betting .notification-panel .close-notification {
  height: 100%;
}
.mod-inline-betting .notification-panel.cancelled .reference {
  color: #1e1e1e;
}
.left-side-column .lhm-collapse {
  background-color: #303030;
  color: #999;
  height: 20px;
}
.left-side-column .lhm-collapse span {
  line-height: 20px;
}
.left-side-column .lhm-action-wrapper {
  background-color: #ccc;
  color: #666;
}
.left-side-column .lhm-action-wrapper:hover {
  background-color: #bfbfbf;
}
.left-side-column .expand-collapse-action {
  cursor: pointer;
}
.left-side-column .hide-label {
  padding-left: 8px;
}
.left-side-column .other-actions {
  display: none;
}
.left-side-column .collapse-arrow {
  transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transition: transform 0.2s ease;
  -moz-transition: transform 0.2s ease;
  -webkit-transition: transform 0.2s ease;
}
.left-side-column .shortcut-icon-wrapper {
  float: right;
  width: 16px;
  height: 16px;
  padding-left: 4px;
  padding-top: 4px;
  margin-right: 4px;
}
.left-side-column .shortcut-icon {
  position: relative;
  overflow: hidden;
  width: 12px;
  height: 12px;
  fill: #999;
}
.left-side-column.is-collapsed {
  width: 36px;
  background-color: #303030;
}
.left-side-column.is-collapsed .hidden-when-left-side-collapsed {
  display: none;
}
.left-side-column.is-collapsed .lhm-collapse {
  margin-bottom: 0;
  padding-left: 0;
  height: auto;
  display: block;
  background-color: #dfdfdf;
}
.left-side-column.is-collapsed .lhm-action-wrapper {
  height: 100%;
  background-color: #303030;
}
.left-side-column.is-collapsed .lhm-action-wrapper::before {
  content: " ";
  height: 6px;
  display: block;
}
.left-side-column.is-collapsed .hide-label {
  display: none;
}
.left-side-column.is-collapsed .other-actions {
  display: block;
}
.left-side-column.is-collapsed .collapse-arrow-wrapper .shortcut-icon {
  transform: rotate(-90deg);
  -ms-transform: rotate(-90deg);
}
.left-side-column.is-collapsed .shortcut-icon-wrapper {
  width: 22px;
  height: 22px;
  border-radius: 2px;
  padding-top: 6px;
  padding-left: 6px;
  margin-left: 4px;
  cursor: pointer;
}
.left-side-column.is-collapsed .shortcut-icon-wrapper .shortcut-icon {
  display: block;
  position: relative;
  overflow: hidden;
  width: 16px;
  height: 16px;
  fill: #999;
}
.left-side-column.is-collapsed .shortcut-icon-wrapper:hover {
  background-color: #4d4d4d;
}
.left-side-column.is-collapsed
  .shortcut-icon-wrapper:hover:not(.active)
  .shortcut-icon {
  fill: #fff;
}
.left-side-column.is-collapsed .shortcut-icon-wrapper.active .favourite-icon {
  fill: #fdb714;
}
.live-stream-container {
  transition: all 300ms ease-in-out;
  -moz-transition: all 300ms ease-in-out;
  -webkit-transition: all 300ms ease-in-out;
  position: relative;
  background: #000;
  min-height: 209px;
  zoom: 1;
}
.live-stream-container.animate-toggle {
  height: 0 !important;
  opacity: 0;
}
.live-stream-container::after {
  content: ".";
  display: block;
  clear: both;
  overflow: hidden;
  line-height: 0;
  height: 0;
}
.live-stream-container .live-stream-header {
  height: 24px;
  line-height: 24px;
  padding: 0 8px;
  background: #303030;
}
.live-stream-container .live-stream-header .live-stream-title {
  padding-right: 12px;
  font-weight: 700;
  font-size: 12px;
  color: #fff;
}
.live-stream-container .tabs li {
  background: #454545;
  height: 24px;
  line-height: 24px;
  font-size: 12px;
  font-weight: 700;
  float: left;
  text-align: center;
  color: #fff;
  cursor: pointer;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  padding: 0 10px;
  box-sizing: border-box;
}
.live-stream-container .tabs li.selected {
  background: linear-gradient(0deg, #c1c1c1, #dfdfdf);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#dfdfdf", endColorstr="#c1c1c1", GradientType=0);
  color: #1e1e1e;
  cursor: default;
  pointer-events: none;
}
.live-stream-container .bf-row {
  margin: 0;
}
.live-stream-container .tabs-container {
  float: left;
  clear: left;
  text-align: center;
}
.live-stream-container .tabs-container iframe {
  border: 0;
  overflow: hidden;
  display: inline-block;
}
.live-stream-container .tabs-container .not-loggedin {
  color: #fff;
  font-size: 12px;
  padding: 80px 20px;
  line-height: 1.4;
  box-sizing: border-box;
}
.live-stream-container .live-stream-play {
  color: #fff;
  text-align: center;
}
.live-stream-container .live-stream-play .icon-play {
  width: 50px;
  height: 50px;
  background: transparent url(images/app/modules/live-stream/play_4627_.png)
    no-repeat top center;
  margin-top: 40px;
  margin-bottom: 30px;
  display: inline-block;
  cursor: pointer;
}
.live-stream-container .live-stream-play p {
  line-height: 1.4;
}
.live-stream-container .live-stream-play a {
  color: #2489d5;
}
.bf-section-header .live-stream-popup {
  color: #4eb6ff;
  font-size: 11px;
  text-decoration: none;
  line-height: 24px;
  padding-left: 12px;
  cursor: pointer;
}
.bf-section-header .live-stream-popup:hover {
  text-decoration: underline;
}
.login-dialog .left {
  float: left;
  margin-top: 5px;
  margin-left: 7px;
  margin-right: 12px;
}
.login-dialog .left .title {
  margin-bottom: 10px;
  font-size: 14px;
  font-weight: 700;
  line-height: 24px;
}
.login-dialog .left .label-text {
  width: 200px;
  height: 13px;
  margin-bottom: 3px;
  display: block;
  font-size: 11px;
  color: #7e97a7;
}
.login-dialog .left .login-input {
  height: 13px;
  border-radius: 3px;
  border: 1px solid #939ca3;
  box-shadow: 0 2px 0 #fff inset;
  margin-bottom: 5px;
  padding: 3px 8px 4px;
  cursor: text;
  width: 185px;
  background: linear-gradient(0deg, #fff, #eaf0f5);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#eaf0f5", endColorstr="white", GradientType=0);
  background-origin: padding-box;
  background-size: auto;
}
.login-dialog .left .login-button {
  border: 1px solid;
  color: #273a47;
  overflow: visible;
  background: #ffe659;
  background: linear-gradient(0deg, #fff, #ffb80c);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#ffb80c", endColorstr="white", GradientType=0);
  zoom: 1;
  border-radius: 3px;
  cursor: pointer;
  border-color: #fa2 #fa2 #bf7c12;
  padding: 2px 5px;
  margin: 5px 0 10px;
  width: auto;
  font-weight: 700;
}
.login-dialog .left .security-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -39px;
  width: 10px;
  height: 13px;
  display: inline-block;
}
.login-dialog .left .forgot-link {
  color: #2789ce;
  font-size: 11px;
  -webkit-text-decoration: none solid #2789ce;
  text-decoration: none solid #2789ce;
}
.login-dialog .right {
  width: 205px;
  height: 174px;
  padding-left: 16px;
  padding-right: 10px;
  border-left: 1px;
  border-left-color: #c7d5e0;
  border-left-style: solid;
  float: right;
}
.login-dialog .right .title {
  margin-bottom: 10px;
  font-size: 14px;
  font-weight: 700;
  line-height: 24px;
  display: block;
}
.login-dialog .right .first-text,
.login-dialog .right .second-text {
  font-weight: 700;
  margin-bottom: 16px;
  display: block;
}
.login-dialog .right .join-now-button {
  border: 1px solid;
  font-weight: 700;
  color: #273a47;
  background: linear-gradient(0deg, #fff, #eaf0f5);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#eaf0f5", endColorstr="white", GradientType=0);
  border-radius: 3px;
  border-color: #c6d5e0 #c6d5e0 #8093a0;
  padding: 4px 5px;
  text-decoration: none;
}
.market-navigation-container {
  background-color: #efefef;
}
.market-navigation-container .markets-tabs-container {
  height: 29px;
  border-bottom: 1px solid #dfdfdf;
}
.market-navigation-container::after {
  clear: both;
  display: block;
  content: " ";
}
.market-navigation-container .generic-tabs-container {
  width: inherit;
  clear: inherit;
}
.market-navigation-container .generic-tab {
  height: 29px;
  width: 120px;
  padding: 0;
  text-align: center;
}
.market-navigation-container .generic-tab.small {
  width: 85px;
}
.market-navigation-container .generic-tab.generic-tab-selected {
  border-bottom: 1px solid #fff;
}
.market-navigation-container .generic-tab .market-tab-label {
  padding-top: 2px;
  height: 100%;
  text-decoration: none;
  color: #1e1e1e;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.market-navigation-container .more-tabs {
  position: relative;
  z-index: 2;
}
.market-navigation-container .more-tabs .more-dropdown-button {
  padding: 0 10px 10px 16px;
  color: #1e1e1e;
}
.market-navigation-container
  .more-tabs
  .more-dropdown-button
  .more-dropdown-label {
  padding-top: 2px;
  display: inline-block;
  max-width: 80%;
  text-decoration: none;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.market-navigation-container .more-tabs .more-dropdown-button::after {
  padding-top: 1px;
  content: "";
  border-top: 5px solid #999;
  border-left: 4.5px solid transparent;
  border-right: 4.5px solid transparent;
  margin-left: 4px;
  vertical-align: middle;
}
.market-navigation-container .more-tabs .dropdown-options {
  position: absolute;
  top: 29px;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.3);
  background: #fff;
  min-width: 100%;
  max-height: 318px;
  overflow: auto;
}
.market-navigation-container .more-tabs .dropdown-options.visible {
  display: block;
}
.market-navigation-container .more-tabs .dropdown-option {
  border-top: 1px solid #e0e6e6;
  color: #1e1e1e;
  line-height: 30px;
  cursor: pointer;
  font-weight: 400;
  text-align: left;
  text-decoration: none;
}
.market-navigation-container .more-tabs .dropdown-option:first-child {
  border-top: 0;
}
.market-navigation-container .more-tabs .dropdown-option:hover {
  background-color: #efefef;
}
.market-rules-container {
  padding: 16px;
}
.market-rules-icon {
  cursor: pointer;
  width: 16px;
  height: 16px;
  display: block;
  border-radius: 2px;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2455px;
}
.market-settings-container {
  position: relative;
  background: #666;
  height: 24px;
  display: block;
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.3);
}
.market-settings-container .refresh-rate-qs {
  display: block;
  visibility: visible;
}
.market-settings-container
  .market-refresh-rate-wrapper
  .market-refresh-rate-container {
  float: right;
  margin: 4px 16px 0 0;
  font-size: 11px;
}
.market-settings-container
  .market-refresh-rate-wrapper
  .market-refresh-rate-container
  .label {
  color: #fff;
  float: left;
  line-height: 18px;
  padding-left: 0;
}
.market-settings-container
  .market-refresh-rate-wrapper
  .market-refresh-rate-container
  .value {
  color: #fff;
  float: left;
  width: 20px;
  padding: 0 4px;
  font-weight: 700;
  line-height: 18px;
}
.market-settings-container .marketview-liquidity-slider-wrapper {
  float: right;
  margin: 4px 4px 0 0;
  font-size: 11px;
}
.market-settings-container .marketview-liquidity-slider-wrapper .slidervalue {
  color: #fff;
  float: left;
  width: 35px;
  padding: 0 4px;
  line-height: 18px;
  font-weight: 700;
}
.market-settings-container
  .marketview-liquidity-slider-wrapper
  .marketview-liquidity-slider-label {
  vertical-align: middle;
  color: #fff;
  float: left;
  line-height: 18px;
}
.market-settings-container
  .marketview-liquidity-slider-wrapper
  .quick-settings-slider {
  width: 70px;
  display: inline-block;
  margin: 0 10px 0 5px;
  vertical-align: sub;
}
.market-settings-container .marketview-liquidity-slider-wrapper .bf-slider {
  vertical-align: middle;
}
.market-settings-container
  .marketview-liquidity-slider-wrapper
  input[type="range"]::-webkit-slider-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.market-settings-container
  .marketview-liquidity-slider-wrapper
  input[type="range"]::-moz-range-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.market-settings-container
  .marketview-liquidity-slider-wrapper
  input[type="range"]::-ms-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.market-settings-container .close-container {
  margin: 5px 0 4px;
  border-left: 1px gray solid;
  float: right;
  width: 24px;
  height: 15px;
  text-align: center;
}
.market-settings-container .close-container .close-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1998px;
  margin: 4px 0 0;
  border: 0;
  padding: 0;
  width: 8px;
  height: 8px;
  outline: 0;
}
.market-settings-container .default-stake-preference {
  float: left;
  margin: 5px 12px 0 8px;
}
.market-settings-container .default-stake-preference label {
  color: #fff;
}
.market-settings-container .default-stakes-container {
  float: left;
  margin: 4px 4px 0 0;
}
.notification-message-container {
  height: 23px;
  background: #fff8d6;
  border-top: 1px solid rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
  z-index: 1;
  font-size: 11px;
}
.notification-message-container .notification-message {
  color: #1e1e1e;
  line-height: 23px;
  padding: 0 8px;
  float: left;
  max-width: 75%;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.notification-message-container .undo-button {
  float: right;
  padding: 0 8px;
  margin: 4px 8px;
  line-height: 16px;
  border: 0;
  cursor: pointer;
  border-radius: 2px;
  color: #1e1e1e;
  outline: 0;
  background: #bfbfbf;
}
.notification-message-container .close-container {
  margin: 4px 0;
  border-left: 1px #bbb solid;
  float: right;
  width: 23px;
  height: 15px;
  text-align: center;
}
.notification-message-container .close-container .close-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -2023px;
  margin: 4px 0 0;
  border: 0;
  padding: 0;
  width: 8px;
  height: 8px;
  outline: 0;
}
.market-settings-space {
  overflow: visible;
  height: calc(100% - 24px);
  height: -webkit-calc(100% - 24px);
}
.market-settings-space.module-loading-spinner {
  height: 100%;
}
@media only screen and (max-width: 1230px) {
  .market-settings-container .marketview-liquidity-slider-wrapper {
    display: none;
  }
}
@media only screen and (max-width: 1279px) {
  html[lang="da-dk"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper,
  html[lang="pt-pt"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper,
  html[lang="sv-se"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper {
    display: none;
  }
}
@media only screen and (max-width: 1365px) {
  html[lang="bg-bg"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper,
  html[lang="de-de"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper,
  html[lang="es-es"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper,
  html[lang="it-it"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper,
  html[lang="ru-ru"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper {
    display: none;
  }
}
@media only screen and (max-width: 1390px) {
  html[lang="el-gr"]
    .market-settings-container
    .marketview-liquidity-slider-wrapper {
    display: none;
  }
}
@media only screen and (max-width: 1470px) {
  .market-settings-container .market-refresh-rate-wrapper {
    display: none;
  }
}
@media only screen and (max-width: 1620px) {
  html[lang="da-dk"] .market-settings-container .market-refresh-rate-wrapper,
  html[lang="pt-pt"] .market-settings-container .market-refresh-rate-wrapper,
  html[lang="sv-se"] .market-settings-container .market-refresh-rate-wrapper {
    display: none;
  }
}
@media only screen and (max-width: 1680px) {
  html[lang="bg-bg"] .market-settings-container .market-refresh-rate-wrapper,
  html[lang="de-de"] .market-settings-container .market-refresh-rate-wrapper,
  html[lang="es-es"] .market-settings-container .market-refresh-rate-wrapper {
    display: none;
  }
}
@media only screen and (max-width: 1730px) {
  html[lang="el-gr"] .market-settings-container .market-refresh-rate-wrapper,
  html[lang="it-it"] .market-settings-container .market-refresh-rate-wrapper {
    display: none;
  }
}
@media only screen and (max-width: 1790px) {
  html[lang="ru-ru"] .market-settings-container .market-refresh-rate-wrapper {
    display: none;
  }
}
.favourites-listing {
  border: 1px solid #dfdfdf;
}
.favourites-listing .fav-container {
  overflow-y: auto;
  height: 409px;
}
.favourites-listing .fav-container .fav-list-items {
  display: block;
}
.favourites-listing .fav-container .fav-list-items .fav-item-container:hover {
  background-color: #f6f6f6;
}
.favourites-listing .fav-container .fav-list-items .fav-item {
  padding: 0;
  border-bottom: 1px solid #eee;
  border-top: 0;
}
.favourites-listing .fav-container .fav-list-items .fav-item.fav-item-parent {
  border-bottom: 1px solid #e0e6e6;
}
.favourites-listing .fav-container .fav-list-items .fav-item .fav-item-remove {
  outline: 0;
  width: 12px;
  height: 12px;
  float: right;
  margin-top: 4px;
  margin-right: 12px;
  border-width: 0;
  background: url(images/app/common/assets/svgs/favourites/favourite-delete-parent-normal_4627_.svg)
    0 0 no-repeat;
}
.favourites-listing
  .fav-container
  .fav-list-items
  .fav-item
  .fav-item-remove:hover {
  background: url(images/app/common/assets/svgs/favourites/favourite-delete-parent-active_4627_.svg)
    0 0 no-repeat;
}
.favourites-listing .fav-container .fav-list-items .fav-item .fav-sub-item {
  padding-left: 20px;
  line-height: 20px;
  border-top: 1px solid #fff;
  color: #666;
}
.favourites-listing
  .fav-container
  .fav-list-items
  .fav-item
  .fav-sub-item:hover {
  background-color: #f6f6f6;
}
.favourites-listing
  .fav-container
  .fav-list-items
  .fav-item
  .fav-sub-item
  .fav-item-remove {
  background: url(images/app/common/assets/svgs/favourites/favourite-delete-child-normal_4627_.svg)
    0 0 no-repeat;
}
.favourites-listing
  .fav-container
  .fav-list-items
  .fav-item
  .fav-sub-item
  .fav-item-remove:hover {
  background: url(images/app/common/assets/svgs/favourites/favourite-delete-child-active_4627_.svg)
    0 0 no-repeat;
}
.favourites-listing .fav-container .fav-list-items .fav-item .fav-item-label {
  line-height: 20px;
  padding-left: 8px;
}
.favourites-listing
  .fav-container
  .fav-list-items
  .fav-item
  .fav-list-sub-items {
  display: block;
}
.favourites-listing .fav-container .fav-list-items.fav-list-drag-and-drop {
  cursor: move;
}
.favourites-listing
  .fav-container
  .fav-list-items.fav-list-drag-and-drop
  .fav-item-container {
  background: url(images/app/common/assets/svgs/favourites/favourite-drag-normal_4627_.svg)
    0 0 no-repeat;
  background-position: 8px 4px;
}
.favourites-listing
  .fav-container
  .fav-list-items.fav-list-drag-and-drop
  .fav-item-container:active {
  background: url(images/app/common/assets/svgs/favourites/favourite-drag-active_4627_.svg)
    0 0 no-repeat;
  background-position: 8px 4px;
}
.favourites-listing
  .fav-container
  .fav-list-items.fav-list-drag-and-drop
  .fav-item-container
  .fav-item-label {
  padding-left: 16px;
}
.favourites-listing
  .fav-container
  .fav-list-items.fav-list-drag-and-drop
  .bf-list-drag-and-drop-target-placeholder {
  border: 1px solid #ffb80c;
}
.favourites-listing
  .fav-container
  .fav-list-items.fav-list-drag-and-drop
  .bf-list-drag-and-drop-dragging
  .fav-item {
  background-color: #dfdfdf;
}
.favourites-listing
  .fav-container
  .fav-list-items.fav-list-drag-and-drop
  .bf-list-drag-and-drop-dragging
  .fav-item.fav-item-parent
  .fav-item-container {
  background-color: #ccc;
}
.favourites-listing .fav-listing-button {
  height: 40px;
  bottom: 0;
  left: 0;
  right: 0;
  background: #efefef;
  border-top: 1px solid #dfdfdf;
}
.favourites-listing .fav-listing-button .favourites-listing-remove-all-btn,
.favourites-listing .fav-listing-button .favourites-listing-submit-btn {
  display: inline;
  float: right;
  margin-top: 8px;
}
.favourites-listing .fav-listing-noresult {
  font-size: 11px;
  line-height: 12px;
  color: #1e1e1e;
  margin-top: 50%;
  text-align: center;
}
.favourites-listing .fav-listing-noresult .star {
  background: url(images/app/common/assets/svgs/favourites/favourite-normal_4627_.svg)
    0 0 no-repeat;
  width: 12px;
  height: 12px;
  display: inline-block;
}
.my-markets-manager-modal-dialog .my-markets-manager-navigation {
  margin-right: 16px;
}
.my-markets-manager-modal-dialog .close-dialog {
  border-radius: 0;
  width: 12px;
  height: 12px;
  border-width: 0;
  color: transparent;
}
.my-markets-manager-modal-dialog .my-markets-manager-container {
  padding: 0;
  height: 450px;
  font-size: 11px;
}
.my-markets-manager-modal-dialog .fav-container {
  margin: 0;
  padding: 0;
}
.my-markets-manager-modal-dialog .my-markets-manager-subheader {
  margin-bottom: 8px;
  min-height: 27px;
}
.my-markets-manager-modal-dialog
  .my-markets-manager-subheader
  .my-markets-manager-subtitle {
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 2px;
}
.my-markets-manager-modal-dialog
  .my-markets-manager-subheader
  .my-markets-manager-info {
  font-size: 11px;
  line-height: 12px;
  color: #1e1e1e;
}
.my-markets-manager-modal-dialog .my-markets-manager-subheader .star {
  background: url(images/app/common/assets/svgs/favourites/favourite-normal_4627_.svg)
    0 0 no-repeat;
  width: 12px;
  height: 12px;
  display: inline-block;
}
.favourites-container {
  background-color: #fff;
  height: calc(100% - 20px);
}
.favourites-container .favourites-inner-container {
  height: 100%;
}
.favourites-container .fake-my-markets {
  width: 100%;
}
.favourites-container .fake-my-markets .fake-title {
  background-color: #acacac;
  height: 20px;
}
.favourites-container .favourites-section {
  height: calc(100% - 20px);
  width: 100%;
}
.favourites-container .favourites-title {
  background: #303030;
  border-bottom: 1px solid #e0e6e6;
  color: #fff;
  padding: 3px 3px 2px 8px;
  cursor: pointer;
  line-height: 15px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  -o-user-select: none;
  user-select: none;
}
.favourites-container .favourites-title:hover {
  background: #1e1e1e;
  color: #f6f6f6;
}
.favourites-container .favourites-title .star-icon {
  background: url(images/app/common/assets/svgs/favourites/favourite-active_4627_.svg)
    0 0 no-repeat;
  width: 12px;
  height: 12px;
  float: left;
  margin-top: 1px;
  margin-right: 5px;
}
.favourites-container .favourites-title .star-icon.disabled {
  background: url(images/app/common/assets/svgs/favourites/favourite-disabled_4627_.svg)
    0 0 no-repeat;
}
.favourites-container .favourites-title .expand-arrow {
  width: 12px;
  height: 12px;
  float: right;
  margin: 2px 5px 0 0;
  transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transition: all 0.2s ease;
  -moz-transition: all 0.2s ease;
  -webkit-transition: all 0.2s ease;
}
.favourites-container.collapsed {
  height: 20px;
}
.favourites-container.collapsed .favourites-section {
  display: none;
}
.favourites-container.collapsed .favourites-title .expand-arrow {
  transform: rotate(0deg);
  -ms-transform: rotate(0deg);
}
.favourites-container .favourites-list {
  height: calc(100% - 20px);
  overflow-y: auto;
}
.favourites-container .item-link {
  border-bottom: 1px solid #e0e6e6;
  color: #303030;
  display: block;
  font-weight: 400;
  text-decoration: none;
  padding: 4px 3px 4px 8px;
  cursor: pointer;
}
.favourites-container .item-link.selected {
  font-weight: 700;
}
.favourites-container .manage-fav-bt {
  zoom: 1;
  cursor: pointer;
  border-bottom: 1px solid #e0e6e6;
}
.favourites-container .manage-fav-bt::after {
  content: ".";
  display: block;
  clear: both;
  overflow: hidden;
  line-height: 0;
  height: 0;
}
.favourites-container .manage-fav-bt .item-link {
  float: left;
  border-bottom: 0;
}
.favourites-container .manage-fav-bt .cog-icon {
  background: url(images/app/common/assets/svgs/lhm/gear-btn_4627_.svg) 0 0
    no-repeat;
  width: 12px;
  height: 12px;
  float: right;
  margin-top: 3px;
  margin-right: 3px;
}
.favourites-container .manage-fav-bt:hover {
  background-color: #f6f6f6;
}
.favourites-container .title-group {
  color: #000;
  display: block;
  text-decoration: none;
  padding: 3px 3px 3px 8px;
  border-bottom: 1px solid #fff;
}
.favourites-container a.title-group:hover {
  cursor: pointer;
  background-color: #f6f6f6;
  color: #3d8acf;
}
.favourites-container .item-link-grouped {
  color: #666;
  display: block;
  font-weight: 400;
  text-decoration: none;
  padding: 3px 3px 3px 16px;
  cursor: pointer;
  border-bottom: 1px solid #fff;
}
.favourites-container .item-link-grouped.selected {
  color: #303030;
  font-weight: 700;
}
.favourites-container .item-link-grouped:hover {
  background-color: #f6f6f6;
  color: #3d8acf;
}
.favourites-container li > div:last-child .fav-item,
.favourites-container li > div:last-child .item-link-grouped {
  border-bottom: 1px solid #e0e6e6;
}
.favourites-container .item-link:hover {
  background-color: #f6f6f6;
  color: #3d8acf;
}
.favourites-container .no-favourites {
  padding: 5px 3px 5px 8px;
  background-color: #fff;
  line-height: 15px;
  color: #939ca3;
}
.favourites-container .no-favourites .manage-favourites-link {
  color: #2789ce;
  cursor: pointer;
}
.navigation-extra-links-container .bottom-navigation {
  width: 100%;
}
.navigation-extra-links-container
  .bottom-navigation
  .navigation-link.bottom-navigation-link {
  background-color: #303030;
  color: #fff;
  border-top: 1px solid #4d4d4d;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.navigation-extra-links-container
  .bottom-navigation
  .navigation-link.bottom-navigation-link:hover {
  color: #f6f6f6;
  background-color: #1e1e1e;
}
.navigation-extra-links-container .bottom-navigation .node {
  cursor: pointer;
  position: relative;
}
.navigation-extra-links-container .bottom-navigation .node .navigation-link {
  padding: 3px 20px 2px 8px;
  display: block;
  text-decoration: none;
  color: #f6f6f6;
  position: relative;
  line-height: 15px;
}
.navigation-extra-links-container
  .bottom-navigation
  .node
  .navigation-link:hover {
  background-color: #1e1e1e;
}
.accordion-pane-links-4,
.extra-links-space-4 {
  height: calc(100% - 124px);
  height: -webkit-calc(100% - 124px);
}
.accordion-pane-links-3,
.extra-links-space-3 {
  height: calc(100% - 103px);
  height: -webkit-calc(100% - 103px);
}
.accordion-pane-links-2,
.extra-links-space-2 {
  height: calc(100% - 82px);
  height: -webkit-calc(100% - 82px);
}
.accordion-pane-links-1,
.extra-links-space-1 {
  height: calc(100% - 61px);
  height: -webkit-calc(100% - 61px);
}
.accordion-pane-links-0,
.extra-links-space-0 {
  height: calc(100% - 40px);
  height: -webkit-calc(100% - 40px);
}
.collapsed-pane {
  height: 20px;
}
.fake-navigation-extra-links {
  width: 100%;
}
.fake-navigation-extra-links .fake-node {
  background-color: #acacac;
  height: 20px;
  border-top: 1px solid #f4f4f4;
}
.navigation-container::before {
  content: " ";
  height: 100%;
  float: left;
}
.navigation-container {
  height: 100%;
  background: #fff;
}
.navigation-container .navigation-title {
  background-color: #303030;
  color: #fff;
  padding: 2px 8px 3px;
  cursor: pointer;
  position: relative;
  line-height: 15px;
  border-top: 1px solid #4d4d4d;
}
.navigation-container .navigation-title:hover {
  background-color: #1e1e1e;
  color: #f6f6f6;
}
.navigation-container .expand-arrow {
  width: 12px;
  height: 12px;
  float: right;
  display: none;
}
.navigation-container .navigation-content .section {
  max-height: 100%;
}
.navigation-container .navigation-content .section .node {
  position: relative;
}
.navigation-container .navigation-content .section .node .navigation-link {
  padding: 3px 20px 2px 8px;
  display: block;
  text-decoration: none;
  color: #2789ce;
  position: relative;
  line-height: 15px;
  cursor: pointer;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link:hover {
  background-color: #f6f6f6;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link.selected {
  font-weight: 700;
  color: #303030;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link.toggle-node {
  color: #303030;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link.active-node {
  color: #303030;
  font-weight: 700;
  background-color: transparent;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link.navigation-link-disabled {
  cursor: default;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link.disabled {
  color: #7f7f7f;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link.section-header {
  cursor: default;
  background-color: #dee5e4;
  color: #303030;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link
  .inplay-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1231px;
  position: absolute;
  width: 13px;
  height: 13px;
  top: 4px;
  right: 3px;
}
.navigation-container
  .navigation-content
  .section
  .node
  .navigation-link
  .inplay-icon.inplay {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1218px;
}
.navigation-container .arrow-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -598px;
  width: 8px;
  height: 4px;
  position: absolute;
  top: 8px;
  right: 6px;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.active-section {
  overflow-y: auto;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.active-section.hide {
  display: none;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.active-section.section-separator {
  border-top: 1px solid #7f7f7f;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.active-section
  .node
  .navigation-link {
  border-bottom: 1px solid #dfdfdf;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.active-section
  .toggle-node.open {
  border-bottom: 1px solid #fff;
  background-color: #dfdfdf;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.active-section
  .toggle-node.open
  .arrow-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -602px;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section
  .node.horse-racing
  .navigation-link.active-node {
  font-weight: 400;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.toggle-content {
  overflow: hidden;
  background-color: #efefef;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.toggle-content
  .node
  .navigation-link {
  padding-left: 16px;
  border-bottom: 1px solid #fff;
}
.navigation-container
  .navigation-content
  .top-navigation
  .section.toggle-content
  .node:last-child
  .navigation-link {
  border-bottom: 1px solid #e0e6e6;
}
.navigation-container .nested-scrollable-panes-wrapper {
  height: 100%;
}
.navigation-container .collapsed {
  height: 20px;
}
.navigation-container .collapsed .top-navigation {
  height: 0;
}
.navigation-container .collapsed .expand-arrow {
  display: inline-block;
  transform: rotate(0deg);
  -ms-transform: rotate(0deg);
}
.navigation-container .collapsed .navigation-content {
  display: none;
}
.fake-navigation-lhm {
  height: 100%;
  background: #fff;
}
.fake-navigation-lhm .fake-header {
  background-color: #acacac;
  height: 20px;
  border-top: 1px solid #f4f4f4;
}
.navigation-lhm {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-flow: column;
  flex-flow: column;
  height: calc(100% - 20px);
  height: -webkit-calc(100% - 20px);
}
.navigation-lhm .history-link {
  display: block;
  cursor: pointer;
  color: #2789ce;
}
.navigation-lhm .history-link:hover {
  background-color: #f6f6f6;
}
.navigation-lhm .history-link.selected {
  font-weight: 700;
  color: #303030;
}
.navigation-lhm .history-link.selected:hover {
  background-color: transparent;
}
.navigation-lhm .history-label {
  display: inline-block;
  line-height: 15px;
  padding: 2px 0 3px 8px;
}
.navigation-lhm .navigation-list {
  height: 100%;
  overflow-y: auto;
}
.navigation-lhm .navigation-item {
  border-bottom: 1px solid #dfdfdf;
}
.navigation-lhm .navigation-link {
  display: block;
  cursor: pointer;
  color: #2789ce;
}
.navigation-lhm .navigation-link:hover {
  background-color: #f6f6f6;
}
.navigation-lhm .navigation-link.selected {
  font-weight: 700;
  color: #303030;
}
.navigation-lhm .navigation-label {
  display: inline-block;
  padding: 2px 0 3px 8px;
  line-height: 15px;
  width: 80%;
}
.navigation-lhm .navigation-icon {
  margin: 3px 3px 0 0;
  float: right;
  width: 13px;
  height: 13px;
}
.navigation-lhm .navigation-icon.going-inplay {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1231px;
}
.navigation-lhm .navigation-icon.inplay {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1218px;
}
.navigation-lhm .navigation-section-title {
  line-height: 15px;
  padding: 2px 20px 3px 8px;
  cursor: default;
  background-color: #dee5e4;
  color: #303030;
}
.navigation-my-markets-container {
  border: 1px solid #dfdfdf;
  height: 449px;
}
.navigation-my-markets-container .search-container {
  border: 5px solid #dfdfdf;
  height: 20px;
}
.navigation-my-markets-container .search-container .search-element {
  background: url(images/app/common/assets/svgs/favourites/search_4627_.svg) 0 0
    no-repeat;
  float: left;
  margin: 4px 4px 0;
  display: inline-block;
  width: 12px;
  height: 14px;
}
.navigation-my-markets-container .search-container .input-element {
  width: 324px;
  bottom: 0;
  border: 0;
  outline: 0;
  font-size: 11px;
  color: #1e1e1e;
  height: 20px;
  line-height: 20px;
}
.navigation-my-markets-container .search-container .input-element::-ms-clear {
  display: none;
}
.navigation-my-markets-container .search-container .close-element {
  background: url(images/app/common/assets/svgs/favourites/search-delete-normal_4627_.svg)
    0 0 no-repeat;
  cursor: pointer;
  float: right;
  margin: 4px 5px 0 0;
  width: 12px;
  height: 12px;
  display: inline-block;
}
.navigation-my-markets-container .search-container .close-element:hover {
  background: url(images/app/common/assets/svgs/favourites/search-delete-active_4627_.svg)
    0 0 no-repeat;
}
.navigation-my-markets-container .my-markets-manager-scrollable {
  height: 419px;
  overflow-y: auto;
}
.navigation-my-markets-container .navigation-my-markets-content .section .node {
  cursor: pointer;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link {
  padding: 3px 10px 2px 8px;
  display: block;
  text-decoration: none;
  color: #2789ce;
  line-height: 15px;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link:hover {
  background-color: #f6f6f6;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.selected {
  font-weight: 700;
  color: #303030;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.toggle-node {
  color: #303030;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.active-node {
  color: #303030;
  font-weight: 700;
  background-color: transparent;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.MARKET,
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.navigation-link-disabled {
  cursor: default;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.MARKET:hover {
  background-color: transparent;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.TOTE {
  cursor: default;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.TOTE:hover {
  background-color: transparent;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.DAILY_COUPON {
  cursor: default;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.DAILY_COUPON:hover {
  background-color: transparent;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.disabled {
  color: #7f7f7f;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link.section-header {
  cursor: default;
  background-color: #dee5e4;
  color: #303030;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link
  .star-icon {
  background: url(images/app/common/assets/svgs/favourites/favourite-active_4627_.svg)
    0 0 no-repeat;
  width: 12px;
  height: 12px;
  margin-top: 4px;
  cursor: pointer;
  float: right;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node
  .navigation-link
  .star-icon.disabled {
  background: url(images/app/common/assets/svgs/favourites/favourite-normal_4627_.svg)
    0 0 no-repeat;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .section
  .node:last-child
  .navigation-link {
  border-bottom: 0;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .top-navigation
  .section.active-section.hide {
  display: none;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .top-navigation
  .section.active-section
  .node
  .navigation-link {
  border-bottom: 1px solid #dfdfdf;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .top-navigation
  .section.active-section
  .toggle-node.open {
  border-bottom: 1px solid #fff;
  background-color: #dfdfdf;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .top-navigation
  .section.active-section
  .toggle-node.open
  .arrow-icon {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -602px;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .top-navigation
  .section.toggle-content {
  font-weight: 400;
  overflow: hidden;
  background-color: #efefef;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .top-navigation
  .section.toggle-content
  .node
  .navigation-link {
  color: #000;
  padding-left: 16px;
  border-bottom: 1px solid #fff;
  font-weight: 400;
}
.navigation-my-markets-container
  .navigation-my-markets-content
  .top-navigation
  .section.toggle-content
  .node:last-child
  .navigation-link {
  border-bottom: 1px solid #e0e6e6;
}
.next-races-container {
  border-radius: 2px;
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
  overflow: hidden;
}
.next-races-container__cards {
  display: -ms-flexbox;
  display: flex;
}
.next-races-container__cards bf-next-race-card:nth-child(1n + 6),
.next-races-container__cards--large bf-next-race-card:nth-child(1n + 5),
.next-races-container__cards--medium bf-next-race-card:nth-child(1n + 4),
.next-races-container__cards--small bf-next-race-card:nth-child(1n + 3) {
  display: none;
}
.other-markets-tab-content {
  margin: 0 8px;
  overflow: hidden;
}
.other-markets-tab-content .column-left,
.other-markets-tab-content .column-right {
  width: calc(50% - 8px);
}
.other-markets-tab-content .column-left #mini-marketview-mod,
.other-markets-tab-content .column-right #mini-marketview-mod {
  width: 100%;
  padding: 0;
  margin-bottom: 8px;
}
.other-markets-tab-content .column-left {
  float: left;
}
.other-markets-tab-content .column-right {
  float: right;
}
.other-markets-empty-tab-content {
  text-align: center;
  margin-top: 37px;
  margin-bottom: 37px;
}
.other-markets-empty-tab-content .no-markets-to-display {
  font-weight: 700;
}
.other-markets-notification-message-container {
  height: 28px;
  width: 100%;
  background: #d4edf7;
  overflow: hidden;
  z-index: 5;
  font-size: 12px;
  color: #31708f;
}
.other-markets-notification-message-container .notification-message {
  line-height: 28px;
  padding: 0 8px;
  float: left;
  max-width: 75%;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.other-markets-notification-message-container .undo-button {
  float: right;
  padding: 4px;
  margin: 2px 4px;
  line-height: 16px;
  border: 0;
  cursor: pointer;
  background: 0 0;
  font-weight: 700;
  color: #167ac6;
  outline: 0;
}
.other-markets-notification-message-container .undo-button:hover {
  color: #3af;
}
.other-markets-notification-message-container .close-container {
  margin: 6px 0;
  float: right;
  width: 24px;
  height: 16px;
  text-align: center;
  border-left: 1px #afcedd solid;
  cursor: pointer;
}
.other-markets-notification-message-container .close-container .close-icon {
  width: 8px;
  height: 8px;
  vertical-align: bottom;
  fill: #85aec3;
}
.other-markets-container .other-markets-header {
  background: #303030;
  padding-left: 8px;
  height: 28px;
  font-weight: 700;
  font-size: 12px;
  color: #fff;
}
.other-markets-container .other-markets-header span {
  line-height: 28px;
  vertical-align: middle;
}
.other-markets-container .other-markets-header .close-container {
  margin: 6px 0;
  float: right;
  width: 24px;
  height: 16px;
  text-align: center;
  cursor: pointer;
}
.other-markets-container .other-markets-header .close-container .close-icon {
  width: 8px;
  height: 8px;
  vertical-align: bottom;
  fill: #dfdfdf;
}
.other-markets-container .other-markets-generic {
  margin: 0 8px 15px;
  overflow: hidden;
}
.other-markets-container .full-other-market-link {
  padding: 0 4px;
  font-size: 11px;
  color: #7f7f7f;
  text-decoration: none;
}
.other-markets-container .other-markets-tabs {
  width: 100%;
  float: left;
  position: relative;
}
.other-markets-container .other-markets-tabs ul .more-dropdown {
  z-index: 10;
}
.other-markets-container .other-markets-tab-overlay {
  position: absolute;
  top: 33px;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(255, 255, 255, 0.5);
  z-index: 11;
}
.mod-promo-banners .promo-banner {
  display: -ms-flexbox;
  display: flex;
  border-radius: 2px 2px 0 0;
}
.mod-promo-banners .fake-banner {
  width: 100%;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
}
.mod-promo-banners .fake-banner .banner-container {
  margin: 0 auto;
}
.mod-promo-banners .fake-banner .fake-image {
  width: 100%;
  margin: auto;
  min-height: 100px;
  display: block;
  background-color: #ebebeb;
}
.mod-promo-banners .fake-banner .fake-description {
  background-color: #fff;
  height: 102px;
}
.mod-promo-banners .fake-promo-banner:nth-child(1),
.mod-promo-banners .promo-banner:nth-child(1) {
  padding-right: 11px;
}
.mod-promo-banners .fake-promo-banner:nth-child(2),
.mod-promo-banners .promo-banner:nth-child(2) {
  padding: 0 5px;
}
.mod-promo-banners .fake-promo-banner:nth-child(3),
.mod-promo-banners .promo-banner:nth-child(3) {
  padding-left: 11px;
}
.mod-promo-banners .fake-promo-banner .promo-banner-container,
.mod-promo-banners .promo-banner .promo-banner-container {
  background: #fff;
}
.mod-promo-banners .promo-banner-list {
  display: -ms-flexbox;
  display: flex;
}
@media only screen and (max-width: 1279px) {
  .mod-promo-banners .fake-promo-banner:nth-child(1),
  .mod-promo-banners .promo-banner:nth-child(1) {
    padding-right: 8px;
  }
  .mod-promo-banners .fake-promo-banner:nth-child(2),
  .mod-promo-banners .promo-banner:nth-child(2) {
    padding: 0 0 0 8px;
  }
  .mod-promo-banners .fake-promo-banner:nth-child(3),
  .mod-promo-banners .promo-banner:nth-child(3) {
    display: none;
  }
}
.fake-quick-links {
  border-radius: 2px;
}
.fake-quick-links .fake-header {
  width: 243px;
  height: 28px;
  background-color: #acacac;
}
.fake-quick-links .fake-content {
  width: 243px;
  height: 360px;
  background-color: #f4f4f4;
}
.race-info-module {
  padding: 0 8px;
}
.race-info-module .section-header {
  background-color: #ececec;
  color: #000;
  font: 700 11px Arial, Helvetica, sans-serif;
  padding: 6px 8px;
  margin: 2px 0 0;
  font-weight: 700;
}
.betting-forecast-container {
  padding: 8px 0 0;
  overflow: hidden;
}
.betting-forecast-container .greyhound-betting-forecast {
  clear: both;
  overflow: hidden;
}
.betting-forecast-container .bt-item {
  display: inline;
  width: 170px;
  height: 18px;
  margin-bottom: 8px;
  float: left;
}
.betting-forecast-container .greyhound-forecast-6,
.betting-forecast-container .greyhound-forecast-over-6 {
  padding: 8px 0;
}
.betting-forecast-container .greyhound-forecast-6 .bt-item:nth-child(4),
.betting-forecast-container .greyhound-forecast-over-6 .bt-item:nth-child(5) {
  clear: both;
}
.betting-forecast-container .bt-runner-name {
  font-weight: 400;
  font-size: 11px;
  margin: 0 6px;
  float: left;
  line-height: 18px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 102px;
}
.betting-forecast-container .bt-runner-price {
  font-weight: 700;
  font-size: 11px;
  float: left;
  line-height: 18px;
}
.betting-forecast-container .greyhound-silk-mini {
  display: block;
  height: 18px;
  width: 18px;
  overflow: hidden;
  float: left;
}
.betting-forecast-container .greyhound-silk-mini-1 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1704px;
}
.betting-forecast-container .greyhound-silk-mini-2 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1722px;
}
.betting-forecast-container .greyhound-silk-mini-3 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1740px;
}
.betting-forecast-container .greyhound-silk-mini-4 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1758px;
}
.betting-forecast-container .greyhound-silk-mini-5 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1776px;
}
.betting-forecast-container .greyhound-silk-mini-6 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1794px;
}
.betting-forecast-container .greyhound-silk-mini-7 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1812px;
}
.betting-forecast-container .greyhound-silk-mini-8 {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1830px;
}
.race-info-container {
  float: left;
  width: 100%;
}
.race-info-container .runner-rating-list {
  padding: 0 8px;
}
.race-info-container .comment {
  padding: 8px;
  line-height: 16px;
}
.race-info-container .runner-rating-item {
  clear: both;
  height: 32px;
  line-height: 32px;
  position: relative;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  overflow: visible;
  border-bottom: 1px solid #e3e8e8;
}
.race-info-container .runner-rating-item .runner-index,
.race-info-container .runner-rating-item .runner-name {
  display: inline-block;
}
.race-info-container .runner-rating-item .runner-index {
  width: 15px;
}
.race-info-container .runner-rating-item .runner-rating {
  position: absolute;
  display: block;
  top: 10px;
  right: 0;
}
.race-info-container .prediction-123 {
  float: left;
  width: 50%;
  border-right: 3px solid #fff;
  -ms-box-sizing: border-box;
  box-sizing: border-box;
}
.race-info-container .race-view {
  float: right;
  width: 50%;
}
.race-info-container .title-section {
  background-color: #ececec;
  color: #000;
  font-weight: 700;
  font-size: 11px;
  padding: 6px 8px;
}
@media only screen and (max-width: 1024px) {
  .betting-forecast-container .greyhound-forecast-6 .bt-item:nth-child(4),
  .betting-forecast-container .greyhound-forecast-over-6 .bt-item:nth-child(5) {
    clear: none;
  }
}
@media only screen and (max-width: 1279px) {
  .betting-forecast-container .greyhound-forecast-6 .bt-item:nth-child(4),
  .betting-forecast-container .greyhound-forecast-over-6 .bt-item:nth-child(5) {
    clear: none;
  }
}
@media only screen and (min-width: 1024px) and (max-width: 1280px) {
  .betting-forecast-container .greyhound-forecast-over-6 .bt-item:nth-child(4),
  .betting-forecast-container .greyhound-forecast-over-6 .bt-item:nth-child(7) {
    clear: both;
  }
}
.settings-container {
  background: #1e1e1e;
  height: 30px;
  position: relative;
}
.settings-container .settings-toggle {
  background: #1e1e1e;
  color: #dfdfdf;
  border: 0;
  font-size: 12px;
  cursor: pointer;
  height: 30px;
  float: right;
  padding: 0 16px;
}
.settings-container .settings-toggle .settings-toggle-text {
  float: left;
  line-height: 24px;
}
.settings-container .settings-toggle .settings-toggle-arrow {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1913px;
  width: 11px;
  height: 7px;
  float: left;
  margin: 11px 0 0 8px;
}
.settings-container .settings-toggle .settings-arrow {
  float: left;
  margin: 8px 0 0 8px;
  transition: all 0.2s ease;
  -moz-transition: all 0.2s ease;
  -webkit-transition: all 0.2s ease;
}
.settings-container .settings-toggle.open .settings-arrow {
  transform: rotate(-180deg);
}
.settings-container .settings-toggle.open .settings-toggle-arrow {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1923px;
}
.settings-container .settings-toggle.active,
.settings-container .settings-toggle:hover.active {
  background-color: #4d4d4d;
  height: 28px;
}
.settings-container .settings-toggle:focus,
.settings-container .settings-toggle:hover {
  background: rgba(246, 246, 246, 0.1);
  outline: 0;
}
.settings-container .settings-panel {
  border-right: 1px solid #ccc;
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.3);
  position: absolute;
  z-index: 10;
  background: #fff;
  top: 30px;
  right: 0;
  margin-bottom: -30px;
  opacity: 1;
  width: 500px;
}
.settings-container .settings-panel .settings-info-logged-out {
  margin-top: -15px;
  margin-bottom: 4px;
  color: #3b5160;
}
.settings-container .tab-navigation .tab-list {
  top: 0;
  left: 0;
  bottom: 0;
  width: 150px;
  padding-top: 48px;
  background-color: #efefef;
  position: absolute;
}
.settings-container .tab-navigation .tab-list .tab-title {
  font-weight: 700;
  font-size: 12px;
  color: #1e1e1e;
  line-height: 28px;
  padding-left: 19px;
  display: block;
  border: 0;
  outline: 0;
  background: 0 0;
  width: 150px;
  text-align: left;
}
.settings-container .tab-navigation .tab-list .tab-title:focus,
.settings-container .tab-navigation .tab-list .tab-title:hover {
  background-color: #e4e4e4;
}
.settings-container .tab-navigation .tab-list .tab-title.active {
  background-color: #fff;
  padding-left: 16px;
  border-left: 2px solid #ffb80c;
}
.settings-container .tab-navigation .tab-content {
  float: right;
  width: 318px;
  min-height: 200px;
  padding: 13px 16px 20px;
}
.settings-container .tab-navigation .tab-content .section-title {
  font-weight: 700;
  font-size: 14px;
  margin-bottom: 22px;
}
.settings-container .tab-navigation .tab-content .section-item {
  padding: 8px 0;
}
.settings-container .tab-navigation .tab-content .section-item:last-child {
  padding-bottom: 0;
}
.settings-container .tab-navigation .tab-content .section-element {
  color: #3b5160;
  vertical-align: middle;
  cursor: pointer;
}
.settings-container .tab-navigation .tab-content label.section-element {
  padding-left: 4px;
}
.settings-container .tab-navigation .tab-content .section-sub-items {
  padding-left: 14px;
  margin: 4px 0;
}
.settings-container .tab-navigation .tab-content label.setting-bet-view-label {
  float: left;
  padding-left: 0;
}
.settings-container .tab-navigation .tab-content .settings-slider {
  width: 70px;
  display: inline-block;
  margin: 0 10px 0 5px;
}
.settings-container .tab-navigation .tab-content .bf-slider {
  vertical-align: middle;
}
.settings-container
  .tab-navigation
  .tab-content
  input[type="range"]::-webkit-slider-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.settings-container
  .tab-navigation
  .tab-content
  input[type="range"]::-moz-range-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.settings-container
  .tab-navigation
  .tab-content
  input[type="range"]::-ms-thumb {
  width: 14px;
  height: 14px;
  top: -2px;
}
.settings-container .tab-navigation .tab-content .help-message-refresh {
  vertical-align: sub;
}
.settings-container .tab-navigation .tab-content .bf-tooltip-parent {
  padding-left: 4px;
}
.settings-container .tab-navigation .tab-content .hint {
  cursor: help;
  color: #2789ce;
  padding: 0 1px;
}
.settings-container .tab-navigation .tab-content .setting-bet-view-value {
  color: #3b5160;
  float: left;
  width: 40px;
  padding: 0 5px;
  font-weight: 700;
}
.settings-container .tab-navigation .tab-content .link-helpers {
  color: #2489d5;
  text-decoration: underline;
  cursor: pointer;
}
.settings-container
  .tab-navigation
  .tab-content
  .market-refresh-rate-container {
  float: left;
}
.settings-container
  .tab-navigation
  .tab-content
  .market-refresh-rate-container
  .label {
  color: #3b5160;
  vertical-align: middle;
  cursor: default;
  float: left;
  padding-left: 0;
}
.settings-container
  .tab-navigation
  .tab-content
  .market-refresh-rate-container
  .value {
  color: #3b5160;
  float: left;
  padding: 0 5px;
  font-weight: 700;
  width: 20px;
}
.settings-container .default-stake-preference label {
  color: #3b5160;
}
.settings-container .default-stakes-container {
  margin: 8px 0 0 17px;
}
.settings-container .settings-panel.logged-in {
  width: 550px;
}
.settings-container .settings-panel.logged-in .tab-content {
  width: 360px;
}
.settings-container .fake-settings {
  background: #acacac;
  height: 30px;
  position: relative;
}
.settings-panel .version-info {
  color: #7f7f7f;
  font-size: 12px;
  position: absolute;
  bottom: 0;
  padding: 0 0 12px 12px;
}
.bf-header-visibility {
  display: block;
  height: 76px;
  background-color: #dfe5e5;
  padding-left: 9999px;
}
@media only screen and (max-width: 896px) {
  .bf-header-visibility {
    height: 103px;
  }
}
.ssc-container .mod-footer .ssc-fw .ssc-fl,
.ssc-container .mod-footer .ssc-fw .ssc-tlc {
  padding-left: 8px;
  padding-right: 8px;
}
.ssc-container .mod-login .ssc-ud .ssc-md .ssc-tlp .ssc-tlpc {
  top: 21px !important;
}
.ssc-container .mod-header #ssc-hw .ssc-myal a,
.ssc-container .ssc-tlpc li {
  line-height: 30px;
}
.ssc-container .mod-footer,
.ssc-container .mod-header {
  z-index: initial;
}
.ssc-loggedIn .mod-login .ssc-ud.ssc-udrl.ssc-ttc {
  z-index: auto;
}
.front-pages .ssc-container .mod-footer,
.front-pages .ssc-container .mod-footer .ssc-fsh,
.front-pages .ssc-container .mod-footer .ssc-fw,
.front-pages .ssc-container .mod-footer .ssc-seos,
.front-pages .ssc-container .mod-footer .ssc-seos .ssc-seotc {
  background: #dfe5e5;
}
.front-pages .ssc-container .ssc-fw .ssc-fal,
.front-pages .ssc-container .ssc-fw .ssc-fbtm {
  border-color: #7f7f7f;
}
.penalties-container {
  padding-left: 8px;
}
.penalties-container .penalties-side-wrapper {
  padding-top: 8px;
  float: left;
}
.penalties-container .score {
  margin: 0 18px;
}
.penalties-container .score.serving-right {
  margin-right: 6px;
}
.penalties-container .score.serving-left {
  margin-left: 6px;
}
.penalties-container .circle {
  margin-bottom: 5px;
  display: inline-block;
  border-radius: 6px;
  width: 6px;
  height: 6px;
  background-color: #0c0;
}
.penalties-side-wrapper .penalties-side-list {
  list-style-type: none;
}
.penalties-side-wrapper .penalties-side-list .penalty-shot {
  height: 18px;
  width: 18px;
  display: inline-block;
  margin-right: 4px;
}
.penalties-side-wrapper .penalties-side-list .penalty-shot.scored {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1455px;
}
.penalties-side-wrapper .penalties-side-list .penalty-shot.missed {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1474px;
}
.penalties-side-wrapper .penalties-side-list .penalty-shot.blank {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1493px;
}
.penalties-side-wrapper .penalties-side-list .penalty-shot:last-child {
  margin-right: 0;
}
.sports-header-container .star-favourites-container .star-favourites {
  position: absolute;
  margin-top: 4px;
}
.sports-header-container sup {
  top: 0;
}
.sports-header-container .icon-broadcast {
  vertical-align: top;
  display: inline-block;
  width: 12px;
  height: 10px;
  margin-top: 7px;
}
.sports-header-container .icon-broadcast .bf-tooltip {
  width: auto;
  white-space: nowrap;
}
.sports-header-container .broadcasts ng-switch {
  display: inline-block;
}
.sports-header-container .sports {
  background: #303030;
  padding: 5px 8px 4px;
  min-height: 50px;
  position: relative;
}
.sports-header-container .sports .button-container {
  box-sizing: border-box;
  padding-left: 5px;
  text-align: right;
}
.sports-header-container .sports .date,
.sports-header-container .sports .time-elapsed {
  color: #fff;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
.sports-header-container .sports .time-elapsed {
  font-size: 18px;
  margin-top: 2px;
  height: 21px;
  line-height: 21px;
  vertical-align: middle;
}
.sports-header-container .sports .inplay .score,
.sports-header-container .sports .inplay .time-elapsed,
.sports-header-container .sports .inplay-label {
  color: #0c0;
}
.sports-header-container .sports .event-header,
.sports-header-container .sports .title {
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  font-size: 20px;
  line-height: 24px;
}
.sports-header-container .sports .event-header.avb,
.sports-header-container .sports .event-header.default,
.sports-header-container .sports .title.avb,
.sports-header-container .sports .title.default {
  text-overflow: ellipsis;
}
.sports-header-container .sports .title {
  padding-left: 22px;
}
.sports-header-container .sports .date,
.sports-header-container .sports .inplay-label {
  font-size: 12px;
  line-height: 18px;
  margin-top: 4px;
}
.sports-header-container .sports .runners .runner-name {
  float: left;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  max-width: calc(100% - 50px);
}
.sports-header-container .sports .runners .rank-number {
  vertical-align: super;
  font-size: 12px;
  line-height: 12px;
  margin-left: 8px;
}
.sports-header-container .sports .runners .circle {
  margin-bottom: 5px;
  display: inline-block;
  border-radius: 6px;
  width: 6px;
  height: 6px;
  background-color: #0c0;
  margin-left: 8px;
}
.sports-header-container .sports .basketball-header .cell,
.sports-header-container .sports .rugby-header .cell {
  width: 38px;
}
.sports-header-container .sports.snooker .cell {
  line-height: 28px;
  height: 28px;
  width: 41px;
  margin: 0 4px;
}
.sports-header-container .sports .scores {
  height: 82px;
  float: right;
  margin-top: -5px;
  margin-bottom: -4px;
  padding-top: 3px;
  background: #1e1e1e;
  box-sizing: border-box;
}
.sports-header-container .sports .scores .cell {
  height: 26px;
  line-height: 26px;
  width: 31px;
  font-size: 20px;
  float: left;
  text-align: center;
  color: #fff;
}
.sports-header-container .sports .scores .points {
  border-right: 1px solid #303030;
  width: 49px;
}
.sports-header-container .sports .scores .points .cell {
  width: 49px;
}
.sports-header-container .sports .scores .description .cell {
  font-size: 9px;
  color: #9d9d9d;
  height: 26px;
}
.sports-header-container .sports .away,
.sports-header-container .sports .description,
.sports-header-container .sports .home {
  float: left;
  clear: left;
}
.sports-header-container .sports .inplay .highlight {
  color: #2bcc20;
}
.sports-header-container .racing .broadcasts .icon-form,
.sports-header-container .racing .broadcasts .icon-livevideo,
.sports-header-container .racing .broadcasts .icon-radio,
.sports-header-container .racing .icon-multiples,
.sports-header-container .racing .icon-tote,
.sports-header-container .sports .icon-head2head,
.sports-header-container .sports .icon-livestream,
.sports-header-container .sports .icon-multiples {
  border-radius: 3px;
  -moz-border-radius: 3px;
  -webkit-border-radius: 3px;
  cursor: pointer;
  color: #1e1e1e;
  text-decoration: none;
  display: inline-block;
  font-size: 11px;
  margin-left: 4px;
}
.sports-header-container .sports .icon-head2head,
.sports-header-container .sports .icon-livestream,
.sports-header-container .sports .icon-multiples {
  vertical-align: top;
  height: 16px;
  line-height: 16px;
  padding: 0 8px;
  margin-top: 4px;
}
.sports-header-container .sports .icon-broadcast {
  background: transparent url(images/app/modules/sports-header/sprite_4627_.png)
    no-repeat 0 -121px;
}
@media (max-width: 1280px) {
  .sports-header-container .sports .icon-livestream {
    max-width: 60px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
}
.sports-header-container .sports .icon-multiples {
  background: #ffb80c;
}
.sports-header-container .racing .broadcasts .icon-form,
.sports-header-container .racing .broadcasts .icon-livevideo,
.sports-header-container .racing .broadcasts .icon-radio,
.sports-header-container .racing .icon-multiples,
.sports-header-container .racing .icon-tote,
.sports-header-container .sports .icon-head2head,
.sports-header-container .sports .icon-livestream {
  background: linear-gradient(0deg, #c3c3c3, #dedede);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#dedede", endColorstr="#c3c3c3", GradientType=0);
}
.sports-header-container .sports .timeline-penalties-container {
  height: 35px;
}
.sports-header-container
  .sports
  .timeline-penalties-container
  .timeline-container {
  border-top: 1px solid #fff;
  position: absolute;
  width: 100%;
  left: 0;
  bottom: 0;
}
.sports-header-container .sports .halftime-fulltime {
  margin-left: 5px;
  color: #fff;
  font-size: 12px;
  line-height: 21px;
}
.sports-header-container .sports .penalties-container {
  background: #303030;
  height: 32px;
  position: relative;
  display: block;
}
.sports-header-container .sports .penalties-container .score {
  color: #0c0;
  font-size: 20px;
  line-height: 32px;
  float: left;
}
.sports-header-container .sports .penalties-container .score.finished {
  color: #fff;
}
.sports-header-container .sports .cricket .cricket-teams {
  color: #fff;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  padding-top: 3px;
}
.sports-header-container .sports .cricket .cricket-teams .team {
  height: 21px;
  font-size: 20px;
  line-height: 19px;
  padding-left: 22px;
  padding-bottom: 5px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.sports-header-container .sports .cricket .inning {
  float: left;
  margin-right: 1px;
  padding-top: 6px;
  background: #1e1e1e;
}
.sports-header-container .sports .cricket .team-innings {
  margin-top: -9px;
  margin-bottom: -7px;
  height: 90px;
  float: right;
  box-sizing: border-box;
}
.sports-header-container .sports .cricket .team-innings .away,
.sports-header-container .sports .cricket .team-innings .description,
.sports-header-container .sports .cricket .team-innings .home {
  float: left;
  clear: left;
}
.sports-header-container .sports .cricket .team-innings .description {
  font-size: 9px;
  color: #9d9d9d;
  line-height: 20px;
}
.sports-header-container .sports .cricket .team-innings .cell {
  padding-left: 10px;
  height: 27px;
  line-height: 27px;
  width: 125px;
  color: #fff;
  font-size: 0;
}
.sports-header-container .sports .cricket .team-innings .cell.highlight {
  color: #2bcc20;
}
.sports-header-container .sports .cricket .team-innings .score-small {
  font-size: 12px;
}
.sports-header-container .sports .cricket .team-innings .score-medium {
  font-size: 16px;
}
.sports-header-container .sports .cricket .team-innings .score-big {
  font-size: 20px;
}
.sports-header-container .sports .cricket .team-innings .score-small-padding {
  font-size: 12px;
  padding-left: 5px;
}
.sports-header-container .sports .tennis-header .tennis-points {
  width: 49px;
  border-left: 1px solid #303030;
  border-right: 1px solid #303030;
}
.sports-header-container .sports .tennis-header .tennis-points .cell {
  width: 49px;
}
.sports-header-container .sports .darts-header .darts-statistics,
.sports-header-container .sports .tennis-header .tennis-statistics {
  width: 132px;
}
.sports-header-container .sports .darts-header .darts-statistics .cell,
.sports-header-container .sports .tennis-header .tennis-statistics .cell {
  width: 44px;
  color: #9d9d9d;
}
.sports-header-container .sports .beach-volleyball-header .scores .cell,
.sports-header-container .sports .volleyball-header .scores .cell {
  width: 34px;
}
.sports-header-container .sports .darts-header .darts-points {
  width: 49px;
  border-right: 1px solid #303030;
}
.sports-header-container .sports .darts-header .darts-points .cell {
  width: 49px;
}
.sports-header-container .sports .darts-header .darts-points-sets.no-sets {
  display: none;
}
.sports-header-container
  .sports
  .darts-header
  .darts-statistics
  .description
  .cell:nth-last-child(1),
.sports-header-container
  .sports
  .darts-header
  .darts-statistics
  .description
  .cell:nth-last-child(2),
.sports-header-container
  .sports
  .tennis-header
  .tennis-statistics
  .description
  .cell:nth-last-child(1),
.sports-header-container
  .sports
  .tennis-header
  .tennis-statistics
  .description
  .cell:nth-last-child(2),
.sports-header-container .sports.snooker .frames .description .cell {
  line-height: 1.2;
  padding-top: 3px;
  box-sizing: border-box;
}
.sports-header-container .sports.snooker .scores {
  height: 86px;
}
.sports-header-container .sports.snooker .title {
  line-height: 28px;
}
.sports-header-container .sports.snooker .current-break,
.sports-header-container .sports.snooker .current-frame,
.sports-header-container .sports.snooker .frames {
  width: 49px;
  float: left;
  border-right: 1px solid #303030;
}
.sports-header-container .sports.snooker .current-break:last-child,
.sports-header-container .sports.snooker .current-frame:last-child,
.sports-header-container .sports.snooker .frames:last-child {
  border-right: 0;
}
.sports-header-container .sports.snooker .current-break .highlight,
.sports-header-container .sports.snooker .current-frame .highlight,
.sports-header-container .sports.snooker .frames .highlight {
  color: #2bcc20;
}
.sports-header-container .sports .american-football-header .points,
.sports-header-container .sports .american-football-header .quarters,
.sports-header-container .sports .basketball-header .points,
.sports-header-container .sports .basketball-header .quarters,
.sports-header-container .sports .rugby-header .points,
.sports-header-container .sports .rugby-header .quarters {
  float: left;
}
.sports-header-container .sports .american-football-header .quarters > div,
.sports-header-container .sports .basketball-header .quarters > div,
.sports-header-container .sports .rugby-header .quarters > div {
  clear: left;
}
.sports-header-container
  .sports
  .american-football-header.stop
  .quarters
  .highlight,
.sports-header-container .sports .basketball-header.stop .quarters .highlight,
.sports-header-container .sports .rugby-header.stop .quarters .highlight {
  color: #fff;
}
.sports-header-container .sports .american-football-header .circle-no-margin {
  margin-left: 0;
}
.sports-header-container .sports .abstract-sports-footer {
  padding-top: 6px;
  font-size: 12px;
}
.sports-header-container .sports .abstract-sports-footer .match-details,
.sports-header-container .sports .abstract-sports-footer .match-status,
.sports-header-container .sports .abstract-sports-footer .time {
  color: #0c0;
}
.sports-header-container .sports .abstract-sports-footer .surface {
  display: inline-block;
  text-transform: lowercase;
  color: #9d9d9d;
}
.sports-header-container
  .sports
  .abstract-sports-footer
  .surface::first-letter {
  text-transform: capitalize;
}
.sports-header-container .sports .abstract-sports-footer .separator {
  padding: 0 2px;
  color: #fff;
}
.sports-header-container .sports .abstract-sports-footer .match-finished {
  color: #fff;
}
.sports-header-container .sports.rugby-league .circle,
.sports-header-container .sports.rugby-union .circle {
  margin-left: 0;
}
.sports-header-container .racing {
  min-height: 59px;
  position: relative;
}
.sports-header-container .racing .broadcasts {
  display: inline-block;
  text-align: right;
  padding: 8px 8px 7px 0;
  float: right;
  width: 38%;
}
.sports-header-container .racing .event-header {
  float: left;
  width: 60%;
}
.sports-header-container .racing .racing-header {
  zoom: 1;
}
.sports-header-container .racing .racing-header::after {
  content: ".";
  display: block;
  clear: both;
  overflow: hidden;
  line-height: 0;
  height: 0;
}
.sports-header-container .racing .antepost-markets .market-name,
.sports-header-container .racing .event-name,
.sports-header-container .racing .event-time,
.sports-header-container .racing .venue-name {
  font-size: 20px;
  line-height: 20px;
}
.sports-header-container .racing .event-info {
  margin: 8px 0 8px 8px;
  font-size: 12px;
  line-height: 18px;
  color: #303030;
}
.sports-header-container .racing .event-info .event-name,
.sports-header-container .racing .event-info .venue-name {
  display: block;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.sports-header-container .racing .event-info .market-name {
  border-left: 1px solid #303030;
  padding-left: 8px;
  margin-left: 6px;
}
.sports-header-container .racing .event-info .race-status:not(.empty) {
  margin-left: 6px;
  padding: 3px 4px;
  font-size: 10px;
  border-radius: 2px;
  color: #fff;
}
.sports-header-container .racing .event-info .race-status:not(.empty).inplay {
  background-color: #090;
}
.sports-header-container .racing .event-info .race-status:not(.empty).delayed {
  background-color: #1e1e1e;
}
.sports-header-container .racing .event-info .race-status:not(.empty).default {
  background-color: #7f7f7f;
}
.sports-header-container .racing .icon-multiples {
  background: #ffb80c;
}
.sports-header-container .racing .broadcasts .icon-form,
.sports-header-container .racing .broadcasts .icon-livevideo,
.sports-header-container .racing .broadcasts .icon-radio,
.sports-header-container .racing .icon-multiples,
.sports-header-container .racing .icon-tote {
  height: 18px;
  margin-bottom: 4px;
  line-height: 18px;
  padding: 0 10px;
  font-weight: 400;
  text-decoration: none;
  display: inline-block;
}
.sports-header-container .racing .broadcasts .icon-form:active,
.sports-header-container .racing .broadcasts .icon-livevideo:active,
.sports-header-container .racing .broadcasts .icon-radio:active,
.sports-header-container .racing .icon-multiples:active,
.sports-header-container .racing .icon-tote:active {
  background: linear-gradient(0deg, #dedede, #c3c3c3);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#c3c3c3", endColorstr="#dedede", GradientType=0);
  color: #1e1e1e;
}
.sports-header-container .racing .icon-broadcast {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -128px;
  height: 12px;
  margin-top: 3px;
}
.sports-header-container .racing .multiples-container {
  display: inline-block;
}
@media only screen and (min-width: 1024px) and (max-width: 1280px) {
  .sports-header-container .racing .event-name {
    font-size: 20px;
    line-height: 20px;
  }
}
@media only screen and (min-width: 1279px) and (max-width: 1440px),
  only screen and (min-width: 1439px) and (max-width: 1600px),
  only screen and (min-width: 1600px) {
  .sports-header-container .racing .event-name {
    font-size: 24px;
    line-height: 24px;
  }
  .sports-header-container .snooker .scores .cell,
  .sports-header-container .snooker .title {
    font-size: 24px;
  }
}
.timeline {
  background: #303030;
  height: 32px;
  position: relative;
  padding: 0 5px;
}
.timeline .half {
  height: 6px;
  float: left;
  box-sizing: border-box;
  position: relative;
  margin-top: 13px;
  margin-bottom: 13px;
  width: 50%;
}
.timeline.extratime .firstHalf,
.timeline.extratime .secondHalf {
  width: 37.5%;
}
.timeline.extratime .extraTimeFirstHalf,
.timeline.extratime .extraTimeSecondHalf {
  width: 12.5%;
}
.timeline .empty-bar {
  background: linear-gradient(0deg, #9c9c9c, #fff);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#fff", endColorstr="#9c9c9c", GradientType=0);
  height: 5px;
  position: absolute;
  left: 6px;
  right: 6px;
}
.timeline .empty-bar .bar {
  background: linear-gradient(0deg, #087d0e, #0c0);
  -ms-filter: progid:dximagetransform.microsoft.gradient(startColorstr="#0c0", endColorstr="#087d0e", GradientType=0);
  height: 5px;
  max-width: 100%;
}
.timeline .away,
.timeline .home {
  position: absolute;
  width: 18px;
  box-sizing: border-box;
  margin-left: -9px;
}
.timeline .home {
  top: -10px;
}
.timeline .away {
  top: 4px;
}
.timeline .RedCard,
.timeline .YellowCard {
  width: 10px;
  height: 12px;
  margin-left: -5px;
}
.timeline .RedCard {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1527px;
}
.timeline .YellowCard {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1512px;
}
.timeline .Goal {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1542px;
  width: 12px;
  height: 13px;
  margin-left: -6px;
}
.timeline .multiples {
  box-shadow: 0 2px 1px 0 rgba(50, 50, 50, 0.7);
  border-radius: 100px;
  min-width: 11px;
  padding-left: 3px;
  padding-right: 3px;
  background: #fff;
  height: 11px;
  line-height: 12px;
  font-size: 9px;
  text-align: center;
  white-space: nowrap;
  width: auto;
  cursor: default;
}
.timeline .bf-tooltip {
  height: auto;
  font-size: 11px;
  width: auto;
  padding: 3px 6px 5px;
  white-space: nowrap;
  line-height: 15px;
  text-align: left;
  z-index: 50;
}
.timeline .bf-tooltip .match-time {
  color: #090;
  margin-left: 15px;
  margin-top: 2px;
  line-height: 11px;
  display: block;
}
.timeline .bf-tooltip .update-type {
  bottom: 1px;
  position: absolute;
  left: 6px;
}
.timeline .bf-tooltip .team-name {
  color: #1e1e1e;
  margin-left: 15px;
}
.timeline .bf-tooltip > div {
  line-height: 15px;
}
.timeline .home .bf-tooltip {
  margin-bottom: 9px;
}
.timeline .away .bf-tooltip {
  margin-top: 2px;
}
.sports-highlights-coupon {
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
}
.sports-highlights-coupon .card-header-title {
  font-weight: 700;
  border-radius: 2px 2px 0 0;
  font-size: 12px;
  padding: 8px;
  color: #fff;
  background-color: #303030;
}
.sports-highlights-coupon .coupon-cards-empty {
  width: 100%;
  display: table;
  margin-bottom: 3px;
  background-color: #fff;
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
  border-radius: 0 0 2px 2px;
}
.sports-highlights-coupon .coupon-cards-empty p {
  font-size: 12px;
  font-weight: 700;
  color: #1e1e1e;
  height: 89px;
  text-align: center;
  display: table-cell;
  vertical-align: middle;
}
.fake-sports-highlights-coupon {
  border-radius: 2px;
}
.fake-sports-highlights-coupon .fake-header {
  width: 100%;
  height: 28px;
  background-color: #acacac;
}
.fake-sports-highlights-coupon .fake-sub-header {
  width: 100%;
  height: 24px;
  background-color: #f4f4f4;
}
.fake-sports-highlights-coupon .fake-sport-market-list {
  width: 100%;
  display: table;
  border-collapse: collapse;
}
.fake-sports-highlights-coupon .fake-sport-market-list .fake-sport-market {
  display: table-row;
  border-bottom: 1px solid #fff;
}
.fake-sports-highlights-coupon
  .fake-sport-market-list
  .fake-sport-market:last-child {
  border-bottom: 0;
}
.fake-sports-highlights-coupon
  .fake-sport-market-list
  .fake-sport-market
  .fake-schedule {
  width: 61px;
  height: 46px;
  display: table-cell;
  background-color: #f4f4f4;
}
.fake-sports-highlights-coupon
  .fake-sport-market-list
  .fake-sport-market
  .fake-market-data {
  height: 46px;
  display: table-cell;
  background-color: #fff;
}
.star-favourites-container .star-favourites {
  width: 16px;
  height: 16px;
  cursor: pointer;
  margin: 0 6px 0 0;
  border: 0;
}
.star-favourites-container .star-favourites:focus {
  outline: 0;
}
.star-favourites-container.dark .star-favourites {
  display: block;
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -616px;
}
.star-favourites-container.light .star-favourites {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1096px;
}
.star-favourites-container.dark .star-favourites.selected,
.star-favourites-container.dark .star-favourites:hover {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -633px;
}
.star-favourites-container.light .star-favourites.selected,
.star-favourites-container.light .star-favourites:hover {
  background: transparent url(images/app/common/assets/images/sprite_4627_.png)
    no-repeat 0 -1112px;
}
.subnav-wrapper {
  background: #1e1e1e;
  height: 30px;
  overflow: hidden;
  display: block;
  padding: 0;
}
.subnav-wrapper .subnav {
  display: block;
  height: 30px;
  overflow: hidden;
  font-weight: 700;
  font-size: 12px;
}
.subnav-wrapper .subnav .subnav-link {
  float: left;
  padding: 0 10px;
  line-height: 30px;
  border-right: 1px #303030 solid;
  color: #f6f6f6;
  cursor: pointer;
  text-decoration: none;
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.25);
}
.subnav-wrapper .subnav .subnav-first .subnav-link {
  border-left: 1px #303030 solid;
}
.subnav-wrapper .subnav .subnav-link.active:hover,
.subnav-wrapper .subnav .subnav-link:focus,
.subnav-wrapper .subnav .subnav-link:hover {
  background: rgba(246, 246, 246, 0.1);
}
.subnav-wrapper .subnav .subnav-link:active {
  background: #4d4d4d;
}
.subnav-wrapper .fake-subnav {
  background: #acacac;
  height: 30px;
  overflow: hidden;
  display: block;
  padding: 0;
}
.super-coupon {
  position: relative;
}
.super-coupon header .coupon-navigation {
  vertical-align: middle;
  text-align: right;
}
.super-coupon header .coupon-navigation-filter {
  display: inline-block;
  margin: 0 0 8px 8px;
}
.super-coupon header .coupon-navigation-filter:first-child {
  margin-left: 0;
}
.super-coupon header.is-inplay-page .inplay-coupon-navigation {
  -ms-flex: 1 1 auto;
}
.super-coupon header.is-inplay-page .title {
  overflow: visible;
}
.super-coupon .coupon-filter-bar {
  background-color: #fff;
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
  box-sizing: border-box;
  padding: 16px 9px;
}
.super-coupon .coupon-filter-bar::after {
  content: "";
  display: block;
  clear: both;
}
.super-coupon .coupon-filter-bar .bf-select-component .selected-option {
  z-index: 62;
}
.super-coupon .coupon-filter-bar .bf-select-component .select-component-arrow {
  z-index: 63;
}
.super-coupon .coupon-filter-bar .bf-select-component .options-list {
  z-index: 61;
}
.super-coupon .filter-by-form {
  float: right;
  height: 24px;
}
.super-coupon .filter-by-title {
  margin-right: 3px;
}
.super-coupon .filter-by-option {
  font-size: 11px;
  line-height: 24px;
  font-weight: 700;
  border-radius: 2px;
  margin-left: 4px;
  padding: 5px 9px;
  cursor: pointer;
  color: #7f7f7f;
  background-color: #dfdfdf;
  border: solid 1px #dfdfdf;
}
.super-coupon .filter-by-option.selected,
.super-coupon .filter-by-option:hover {
  color: #1e1e1e;
  background-color: #fff;
}
.super-coupon .filter-by-option.disabled {
  color: #7f7f7f;
  background-color: #dfdfdf;
  cursor: default;
  opacity: 0.7;
}
.super-coupon .filter-by-checkbox {
  display: none;
}
.super-coupon .group-by-title {
  float: left;
  margin-top: 6px;
}
.super-coupon .matched-amount-dropdown {
  margin-left: 4px;
}
.super-coupon .matched-amount-dropdown .matched-amount-description {
  margin-bottom: 12px;
}
.super-coupon .matched-amount-dropdown .matched-amount-container {
  margin-bottom: 12px;
  height: 20px;
}
.super-coupon
  .matched-amount-dropdown
  .matched-amount-container
  .matched-amount-label {
  float: left;
  font-weight: 700;
  line-height: 20px;
}
.super-coupon
  .matched-amount-dropdown
  .matched-amount-container
  .matched-amount-input {
  float: right;
  border: solid 1px #dfdfdf;
  border-radius: 2px;
  text-align: center;
  height: 100%;
  width: 40%;
}
.super-coupon
  .matched-amount-dropdown
  .matched-amount-container
  .matched-amount-input:active,
.super-coupon
  .matched-amount-dropdown
  .matched-amount-container
  .matched-amount-input:focus {
  outline: -webkit-focus-ring-color auto 3px;
}
.super-coupon .matched-amount-dropdown .clear-filter-button-container {
  text-align: center;
}
.super-coupon
  .matched-amount-dropdown
  .clear-filter-button-container
  .clear-filter-button {
  min-width: 76px;
  height: 28px;
  font-weight: 700;
  background-color: #bfbfbf;
  color: #1e1e1e;
  border: solid 1px #bfbfbf;
  border-radius: 2px;
  outline: 0;
}
.super-coupon
  .matched-amount-dropdown
  .clear-filter-button-container
  .clear-filter-button:hover {
  background-color: #dfdfdf;
  border: solid 1px #dfdfdf;
}
.super-coupon
  .matched-amount-dropdown
  .bf-dropdown
  .bf-dropdown-title-container {
  padding-top: 6px;
  padding-bottom: 8px;
  z-index: 55;
  min-width: 91px;
  text-align: center;
}
.super-coupon
  .matched-amount-dropdown
  .bf-dropdown
  .bf-dropdown-title-container
  .bf-dropdown-icon {
  top: 6px;
}
.super-coupon .matched-amount-dropdown .bf-dropdown .bf-dropdown-content {
  top: 25px;
  width: 236px;
  z-index: 55;
}
.super-coupon
  .matched-amount-dropdown
  .bf-dropdown
  .bf-dropdown-title-container.is-collapsed {
  padding-top: 7px;
  padding-bottom: 6px;
  background: #dfdfdf;
  color: #7f7f7f;
}
.super-coupon
  .matched-amount-dropdown
  .bf-dropdown
  .bf-dropdown-title-container.is-collapsed
  .bf-dropdown-icon {
  top: 7px;
}
.super-coupon
  .matched-amount-dropdown.selected
  .bf-dropdown
  .bf-dropdown-title-container {
  padding: 6px 24px 5px 8px;
  color: #1e1e1e;
  background-color: #fff;
  border: 1px solid #dfdfdf;
}
.super-coupon
  .matched-amount-dropdown.selected
  .bf-dropdown
  .bf-dropdown-title-container
  .bf-dropdown-icon {
  top: 6px;
  right: 8px;
}
.super-coupon .market-type-filter {
  float: left;
  margin-left: 10px;
}
.super-coupon .group-by-filter {
  float: left;
  margin-left: 8px;
}
.super-coupon .group-by-filter .bf-select-component,
.super-coupon .group-by-filter .bf-select-component .options-list {
  width: 146px;
}
.super-coupon .card-header {
  zoom: 1;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  -o-user-select: none;
  user-select: none;
  font-size: 12px;
  padding: 2px 8px;
  color: #fff;
  background-color: #303030;
  cursor: pointer;
}
.super-coupon .card-header .card-header-multiples::after,
.super-coupon .card-header::after {
  content: ".";
  display: block;
  clear: both;
  overflow: hidden;
  line-height: 0;
  height: 0;
}
.super-coupon .card-header .card-header-title-container {
  float: left;
  line-height: 26px;
}
.super-coupon .card-header .card-header-multiples {
  zoom: 1;
  float: right;
}
.super-coupon
  .card-header
  .card-header-multiples
  .bf-dropdown
  .bf-dropdown-title-container {
  z-index: 52;
}
.super-coupon .card-header .card-header-multiples .bf-dropdown.is-collapsed {
  z-index: 51;
}
.super-coupon .card-header .card-header-multiples .bf-dropdown-content {
  width: 236px;
  color: #1e1e1e;
  cursor: default;
  z-index: 52;
}
.super-coupon .card-header .card-header-multiples-box-title {
  font-weight: 700;
  margin-bottom: 10px;
}
.super-coupon .card-header .card-header-multiples-box-description {
  margin-bottom: 10px;
}
.super-coupon .card-header .card-header-multiples-box-link-container {
  text-align: center;
}
.super-coupon .card-header .card-header-multiples-box-link {
  border-radius: 3px;
  font-weight: 700;
  background: #ffb80c;
  cursor: pointer;
  line-height: 28px;
  padding: 0 10px;
  color: #1e1e1e;
  text-decoration: none;
  display: inline-block;
}
.super-coupon
  .matched-amount-dropdown
  .bf-dropdown.is-collapsed:hover.is-disabled:not
  .bf-dropdown-title-container {
  padding: 6px 24px 5px 8px;
  color: #1e1e1e;
  background-color: #fff;
  border: 1px solid #dfdfdf;
}
.super-coupon
  .matched-amount-dropdown
  .bf-dropdown.is-collapsed:hover.is-disabled:not
  .bf-dropdown-title-container
  .bf-dropdown-icon {
  top: 6px;
  right: 8px;
}
.super-coupon .coupon-card {
  margin-bottom: 16px;
  border-radius: 0 0 2px 2px;
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
}
.super-coupon .coupon-card .card-header {
  font-weight: 700;
  border-radius: 2px 2px 0 0;
}
.super-coupon .coupon-card-first .card-header {
  border-radius: 0;
}
.super-coupon .coupon-card.collapsed .card-header {
  border-bottom-left-radius: 2px;
  border-bottom-right-radius: 2px;
}
.super-coupon .card-header-icon {
  margin-right: 7px;
  transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transition: transform 0.2s ease;
  -moz-transition: transform 0.2s ease;
  -webkit-transition: transform 0.2s ease;
}
.super-coupon .card-header-icon.collapsed {
  transform: rotate(-90deg);
  -ms-transform: rotate(-90deg);
}
.super-coupon .footer-link-container {
  text-align: right;
  font-size: 12px;
  font-weight: 400;
  background-color: #fff;
  border-top: 1px solid #eee;
  padding: 7px 10px 8px;
  border-radius: 0 0 2px 2px;
}
.super-coupon .footer-link-container .footer-link {
  text-decoration: none;
  color: #1e1e1e;
}
.super-coupon .footer-link-container .footer-link:hover {
  text-decoration: underline;
}
.super-coupon .footer-link-container .footer-link-icon {
  fill: #7f7f7f;
  float: right;
  margin: 1px 0 0 6px;
  transform: rotate(180deg);
  -ms-transform: rotate(180deg);
}
.super-coupon .coupon-cards-empty {
  width: 100%;
  display: table;
  margin-bottom: 16px;
  background-color: #fff;
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
  border-radius: 0 0 2px 2px;
}
.super-coupon .coupon-cards-empty .coupon-cards-empty-generic,
.super-coupon .coupon-cards-empty .coupon-cards-empty-reset-filters {
  font-size: 12px;
  font-weight: 700;
  color: #1e1e1e;
  height: 89px;
  text-align: center;
  display: table-cell;
  vertical-align: middle;
}
.super-coupon .coupon-cards-empty .coupon-cards-empty-generic > p,
.super-coupon .coupon-cards-empty .coupon-cards-empty-reset-filters > p {
  line-height: 1.2;
}
.super-coupon
  .coupon-cards-empty
  .coupon-cards-empty-generic
  .coupon-cards-empty-outright,
.super-coupon
  .coupon-cards-empty
  .coupon-cards-empty-reset-filters
  .coupon-cards-empty-outright {
  margin-top: 30px;
}
.super-coupon
  .coupon-cards-empty
  .coupon-cards-empty-generic
  .coupon-cards-empty-outright
  > p,
.super-coupon
  .coupon-cards-empty
  .coupon-cards-empty-reset-filters
  .coupon-cards-empty-outright
  > p {
  line-height: 1.33;
}
.super-coupon
  .coupon-cards-empty
  .coupon-cards-empty-generic
  .coupon-cards-empty-outright
  .coupon-outright-link,
.super-coupon
  .coupon-cards-empty
  .coupon-cards-empty-reset-filters
  .coupon-cards-empty-outright
  .coupon-outright-link {
  display: inline-block;
  height: 28px;
  border-radius: 2px;
  color: #1e1e1e;
  border: 1px solid #bfbfbf;
  background-color: #bfbfbf;
  cursor: pointer;
  box-sizing: border-box;
  padding: 8px 16px 0;
  margin: 20px 0 40px;
  text-decoration: none;
}
.super-coupon
  .coupon-cards-empty
  .coupon-cards-empty-generic
  .coupon-cards-empty-outright
  .coupon-outright-link:hover,
.super-coupon
  .coupon-cards-empty
  .coupon-cards-empty-reset-filters
  .coupon-cards-empty-outright
  .coupon-outright-link:hover {
  border-color: #dfdfdf;
  background-color: #dfdfdf;
}
.super-coupon .coupon-cards-empty .reset-filters {
  border: 0;
  padding: 0;
  background: 0 0;
  color: #167ac6;
}
.super-coupon .coupon-cards-empty .reset-filters:hover {
  text-decoration: underline;
}
@media only screen and (max-width: 1279px) {
  .super-coupon .coupon-filter-bar.has-market-type-filter .filter-by-form {
    clear: left;
    float: none;
    padding-top: 12px;
  }
}
.timeform-module .section-header {
  background-color: #ececec;
  color: #000;
  font: 700 11px Arial, Helvetica, sans-serif;
  padding: 6px 8px;
  margin: 10px 8px 0;
  font-weight: 700;
}
.timeform-container {
  overflow: hidden;
  padding: 0;
  margin: 0;
  color: #273a47;
  font-size: 11px;
  line-height: 16px;
  text-align: left;
  min-height: 250px;
}
.timeform-container .title-section {
  font-weight: 700;
  font-size: 13px;
  color: #273a47;
  border-bottom: 1px solid #e3e8e8;
  text-align: left;
  line-height: 28px;
  margin-bottom: 8px;
}
.timeform-container .text-section {
  margin: 8px 16px 0 0;
  line-height: 16px;
}
.timeform-container .block-container {
  margin: 0 15px 15px;
  overflow: hidden;
}
.timeform-container .timeform-section-123 .runner-rating-list {
  padding-left: 20px;
  margin-top: -8px;
}
.timeform-container .timeform-section-123 .runner-rating-item {
  clear: both;
  height: 32px;
  line-height: 32px;
  list-style-type: decimal;
  position: relative;
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  overflow: visible;
  border-bottom: 1px solid #e3e8e8;
}
.timeform-container .timeform-section-123 .runner-rating-item .runner-rating {
  float: right;
  position: absolute;
  display: block;
  top: 0;
  right: 0;
}
.timeform-container .timeform-section-123 .runner-rating-item .star {
  line-height: 32px;
}
.timeform-container .no-data-available {
  text-align: center;
  padding: 10px 0;
  margin: 0;
  border: 1px solid #f1f3f3;
  background: #f1f3f3;
  font-weight: 700;
  color: #273a47;
}
.timeform-container .timeform-section-comments {
  counter-reset: runner-comments-counter;
}
.timeform-container .timeform-section-comments .columns {
  column-count: 1;
}
.timeform-container .timeform-section-comments .runner-name {
  font-weight: 700;
  counter-increment: runner-comments-counter;
  line-height: 16px;
}
.timeform-container .timeform-section-comments .runner-name::before {
  content: counter(runner-comments-counter);
  margin-right: 5px;
}
.timeform-container .timeform-section-comments .runner-comment {
  margin-bottom: 10px;
  line-height: 16px;
}
@media only screen and (min-width: 1280px) {
  .timeform-container .timeform-section-comments .columns {
    column-count: 2;
  }
}
.todays-racing-load-screen-container {
  width: 100%;
  height: 344px;
  background-color: #fff;
}
.todays-racing-load-screen-container .header {
  width: 100%;
  height: 44px;
  background-color: #acacac;
}
.todays-racing-load-screen-container .content {
  width: 100%;
  height: 300px;
}
.todays-racing-load-screen-container .content .countries {
  width: 100%;
  height: 46px;
  background-color: #f4f4f4;
}
.todays-racing-load-screen-container .content .country-tab {
  float: left;
  width: 86px;
  height: 46px;
  background-color: #fff;
  border-top: 1px solid #fbe3aa;
}
.todays-racing-load-screen-container .country-content {
  width: 100%;
  height: 254px;
}
.todays-racing-mod-container .header {
  height: 28px;
  line-height: 28px;
}
.todays-racing-mod-container .schedule-filter-button {
  text-transform: capitalize;
  border-radius: 2px;
  border: 0;
  background-color: #bfbfbf;
  cursor: pointer;
  box-sizing: border-box;
  padding: 0 16px;
  font-weight: 700;
  text-decoration: none;
  height: 28px;
  font-size: 11px;
  color: #1e1e1e;
}
.todays-racing-mod-container .schedule-filter-button:hover {
  background-color: #dfdfdf;
}
.todays-racing-mod-container .schedule-filter-button:focus {
  outline: 0;
}
.todays-racing-mod-container .schedule-filter-button.active,
.todays-racing-mod-container .schedule-filter-button.active:hover {
  background-color: #fff;
}
.todays-racing-mod-container .todays-racing-loading-countries,
.todays-racing-mod-container .todays-racing-loading-meetings {
  background-image: url(images/app/common/assets/images/betslip_spinner_4627_.gif);
  background-repeat: no-repeat;
  background-position: center center;
  background-color: #fff;
}
.tooltip-step-modal {
  border-radius: 2px;
}
.tooltip-step-modal .tooltip-step-header-container {
  padding: 9px 12px;
  font-size: 14px;
  color: #303030;
  background-color: #dfdfdf;
}
.tooltip-step-modal .tooltip-step-header-container .tooltip-step-close-button {
  top: 10px;
}
.tooltip-step-modal .tooltip-button {
  outline: 0;
}
.tooltip-step-modal .tooltip-button.left-button {
  width: 114px;
  height: 28px;
  border-radius: 2px;
  background-color: #bfbfbf;
  text-overflow: ellipsis;
  overflow: hidden;
}
.tooltip-step-modal .tooltip-button.done-step-button {
  width: 114px;
  height: 28px;
  border-radius: 2px;
  background-color: #ffb80c;
  text-overflow: ellipsis;
  overflow: hidden;
}
.mod-x-sell-banner .x-sell-image {
  width: 243px;
  height: 81px;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.4);
}
.fake-x-sell-banner {
  width: 243px;
  height: 82px;
  background-color: #ebebeb;
}
.x-sell-container {
  position: absolute;
  background-color: #fff;
  top: 30px;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 0 40px;
  overflow: scroll;
}
.x-sell-container .x-sell-mini-header {
  margin: 8px 0 9px 8px;
  font-size: 11px;
  font-weight: 700;
}
.x-sell-container .log-in {
  color: #00f;
  text-decoration: underline;
  cursor: pointer;
}
.x-sell-content {
  position: absolute;
  display: block;
  margin: 0 auto;
  text-align: center;
  top: 30px;
  bottom: 0;
}
.x-sell-games-container {
  position: relative;
  width: 100%;
  padding-top: 1px;
}
.x-sell-games-container .x-sell-games-content {
  transition: all 300ms ease-in-out;
  -moz-transition: all 300ms ease-in-out;
  -webkit-transition: all 300ms ease-in-out;
  height: 120px;
  opacity: 1;
  overflow: hidden;
  background-color: #fff;
}
.x-sell-games-container .x-sell-games-content .x-sell-games-item {
  margin: 8px 0;
  overflow: hidden;
  float: left;
  width: 49%;
  text-align: center;
  cursor: pointer;
}
.x-sell-games-container .x-sell-games-content .x-sell-games-item:first-child {
  margin-left: 3.5%;
}
.x-sell-games-container .x-sell-games-content .x-sell-games-item:last-child {
  margin-left: -3.5%;
}
</style>
<style>
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background: 0 0;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: 700;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid silver;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: 700;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
.bf-row {
  letter-spacing: -0.31em;
  text-rendering: optimizespeed;
  display: -webkit-flex;
  display: -ms-flexbox;
  -ms-flex-flow: row wrap;
  margin-bottom: 10px;
  margin-left: -5px;
  margin-right: -5px;
}
[class*="bf-col-"] {
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
.full-width-page .bf-row {
  margin-left: 0;
  margin-right: 0;
}
.full-width-page [class*="bf-col-"] {
  padding-left: 0;
  padding-right: 0;
}
.bf-col-1,
.bf-col-1-1 {
  width: 100%;
}
.bf-col-1-2 {
  width: 50%;
}
.bf-col-2-2 {
  width: 100%;
}
.bf-col-1-3 {
  width: 33.3333%;
}
.bf-col-2-3 {
  width: 66.6667%;
}
.bf-col-3-3 {
  width: 100%;
}
.bf-col-1-4 {
  width: 25%;
}
.bf-col-2-4 {
  width: 50%;
}
.bf-col-3-4 {
  width: 75%;
}
.bf-col-4-4 {
  width: 100%;
}
.bf-col-1-5 {
  width: 20%;
}
.bf-col-2-5 {
  width: 40%;
}
.bf-col-3-5 {
  width: 60%;
}
.bf-col-4-5 {
  width: 80%;
}
.bf-col-5-5 {
  width: 100%;
}
.bf-col-1-6 {
  width: 16.6667%;
}
.bf-col-2-6 {
  width: 33.3333%;
}
.bf-col-3-6 {
  width: 50%;
}
.bf-col-4-6 {
  width: 66.6667%;
}
.bf-col-5-6 {
  width: 83.3333%;
}
.bf-col-6-6 {
  width: 100%;
}
.bf-col-1-8 {
  width: 12.5%;
}
.bf-col-2-8 {
  width: 25%;
}
.bf-col-3-8 {
  width: 37.5%;
}
.bf-col-4-8 {
  width: 50%;
}
.bf-col-5-8 {
  width: 62.5%;
}
.bf-col-6-8 {
  width: 75%;
}
.bf-col-7-8 {
  width: 87.5%;
}
.bf-col-8-8 {
  width: 100%;
}
.bf-col-1-12 {
  width: 8.3333%;
}
.bf-col-2-12 {
  width: 16.6667%;
}
.bf-col-3-12 {
  width: 25%;
}
.bf-col-4-12 {
  width: 33.3333%;
}
.bf-col-5-12 {
  width: 41.6667%;
}
.bf-col-6-12 {
  width: 50%;
}
.bf-col-7-12 {
  width: 58.3333%;
}
.bf-col-8-12 {
  width: 66.6667%;
}
.bf-col-9-12 {
  width: 75%;
}
.bf-col-10-12 {
  width: 83.3333%;
}
.bf-col-11-12 {
  width: 91.6667%;
}
.bf-col-12-12 {
  width: 100%;
}
.bf-col-1-24 {
  width: 4.1667%;
}
.bf-col-2-24 {
  width: 8.3333%;
}
.bf-col-3-24 {
  width: 12.5%;
}
.bf-col-4-24 {
  width: 16.6667%;
}
.bf-col-5-24 {
  width: 20.8333%;
}
.bf-col-6-24 {
  width: 25%;
}
.bf-col-7-24 {
  width: 29.1667%;
}
.bf-col-8-24 {
  width: 33.3333%;
}
.bf-col-9-24 {
  width: 37.5%;
}
.bf-col-10-24 {
  width: 41.6667%;
}
.bf-col-11-24 {
  width: 45.8333%;
}
.bf-col-12-24 {
  width: 50%;
}
.bf-col-13-24 {
  width: 54.1667%;
}
.bf-col-14-24 {
  width: 58.3333%;
}
.bf-col-15-24 {
  width: 62.5%;
}
.bf-col-16-24 {
  width: 66.6667%;
}
.bf-col-17-24 {
  width: 70.8333%;
}
.bf-col-18-24 {
  width: 75%;
}
.bf-col-19-24 {
  width: 79.1667%;
}
.bf-col-20-24 {
  width: 83.3333%;
}
.bf-col-21-24 {
  width: 87.5%;
}
.bf-col-22-24 {
  width: 91.6667%;
}
.bf-col-23-24 {
  width: 95.8333%;
}
.bf-col-24-24 {
  width: 100%;
}
.hidden,
.visible-block,
.visible-inline,
.visible-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-xl-block,
.visible-xl-inline,
.visible-xl-inline-block,
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-xxl-block,
.visible-xxl-inline,
.visible-xxl-inline-block {
  display: none !important;
}
@media screen and (min-width: 48em) {
  .bf-col-xs-1,
  .bf-col-xs-1-1 {
    width: 100%;
  }
  .bf-col-xs-1-2 {
    width: 50%;
  }
  .bf-col-xs-2-2 {
    width: 100%;
  }
  .bf-col-xs-1-3 {
    width: 33.3333%;
  }
  .bf-col-xs-2-3 {
    width: 66.6667%;
  }
  .bf-col-xs-3-3 {
    width: 100%;
  }
  .bf-col-xs-1-4 {
    width: 25%;
  }
  .bf-col-xs-2-4 {
    width: 50%;
  }
  .bf-col-xs-3-4 {
    width: 75%;
  }
  .bf-col-xs-4-4 {
    width: 100%;
  }
  .bf-col-xs-1-5 {
    width: 20%;
  }
  .bf-col-xs-2-5 {
    width: 40%;
  }
  .bf-col-xs-3-5 {
    width: 60%;
  }
  .bf-col-xs-4-5 {
    width: 80%;
  }
  .bf-col-xs-5-5 {
    width: 100%;
  }
  .bf-col-xs-1-6 {
    width: 16.6667%;
  }
  .bf-col-xs-2-6 {
    width: 33.3333%;
  }
  .bf-col-xs-3-6 {
    width: 50%;
  }
  .bf-col-xs-4-6 {
    width: 66.6667%;
  }
  .bf-col-xs-5-6 {
    width: 83.3333%;
  }
  .bf-col-xs-6-6 {
    width: 100%;
  }
  .bf-col-xs-1-8 {
    width: 12.5%;
  }
  .bf-col-xs-2-8 {
    width: 25%;
  }
  .bf-col-xs-3-8 {
    width: 37.5%;
  }
  .bf-col-xs-4-8 {
    width: 50%;
  }
  .bf-col-xs-5-8 {
    width: 62.5%;
  }
  .bf-col-xs-6-8 {
    width: 75%;
  }
  .bf-col-xs-7-8 {
    width: 87.5%;
  }
  .bf-col-xs-8-8 {
    width: 100%;
  }
  .bf-col-xs-1-12 {
    width: 8.3333%;
  }
  .bf-col-xs-2-12 {
    width: 16.6667%;
  }
  .bf-col-xs-3-12 {
    width: 25%;
  }
  .bf-col-xs-4-12 {
    width: 33.3333%;
  }
  .bf-col-xs-5-12 {
    width: 41.6667%;
  }
  .bf-col-xs-6-12 {
    width: 50%;
  }
  .bf-col-xs-7-12 {
    width: 58.3333%;
  }
  .bf-col-xs-8-12 {
    width: 66.6667%;
  }
  .bf-col-xs-9-12 {
    width: 75%;
  }
  .bf-col-xs-10-12 {
    width: 83.3333%;
  }
  .bf-col-xs-11-12 {
    width: 91.6667%;
  }
  .bf-col-xs-12-12 {
    width: 100%;
  }
  .bf-col-xs-1-24 {
    width: 4.1667%;
  }
  .bf-col-xs-2-24 {
    width: 8.3333%;
  }
  .bf-col-xs-3-24 {
    width: 12.5%;
  }
  .bf-col-xs-4-24 {
    width: 16.6667%;
  }
  .bf-col-xs-5-24 {
    width: 20.8333%;
  }
  .bf-col-xs-6-24 {
    width: 25%;
  }
  .bf-col-xs-7-24 {
    width: 29.1667%;
  }
  .bf-col-xs-8-24 {
    width: 33.3333%;
  }
  .bf-col-xs-9-24 {
    width: 37.5%;
  }
  .bf-col-xs-10-24 {
    width: 41.6667%;
  }
  .bf-col-xs-11-24 {
    width: 45.8333%;
  }
  .bf-col-xs-12-24 {
    width: 50%;
  }
  .bf-col-xs-13-24 {
    width: 54.1667%;
  }
  .bf-col-xs-14-24 {
    width: 58.3333%;
  }
  .bf-col-xs-15-24 {
    width: 62.5%;
  }
  .bf-col-xs-16-24 {
    width: 66.6667%;
  }
  .bf-col-xs-17-24 {
    width: 70.8333%;
  }
  .bf-col-xs-18-24 {
    width: 75%;
  }
  .bf-col-xs-19-24 {
    width: 79.1667%;
  }
  .bf-col-xs-20-24 {
    width: 83.3333%;
  }
  .bf-col-xs-21-24 {
    width: 87.5%;
  }
  .bf-col-xs-22-24 {
    width: 91.6667%;
  }
  .bf-col-xs-23-24 {
    width: 95.8333%;
  }
  .bf-col-xs-24-24 {
    width: 100%;
  }
  .hidden-xs {
    display: none !important;
  }
  .visible-xs-inline-block {
    display: inline-block !important;
  }
  .visible-xs-inline {
    display: inline !important;
  }
  .visible-xs-block {
    display: block !important;
  }
}
@media screen and (min-width: 64em) {
  .bf-col-sm-1,
  .bf-col-sm-1-1 {
    width: 100%;
  }
  .bf-col-sm-1-2 {
    width: 50%;
  }
  .bf-col-sm-2-2 {
    width: 100%;
  }
  .bf-col-sm-1-3 {
    width: 33.3333%;
  }
  .bf-col-sm-2-3 {
    width: 66.6667%;
  }
  .bf-col-sm-3-3 {
    width: 100%;
  }
  .bf-col-sm-1-4 {
    width: 25%;
  }
  .bf-col-sm-2-4 {
    width: 50%;
  }
  .bf-col-sm-3-4 {
    width: 75%;
  }
  .bf-col-sm-4-4 {
    width: 100%;
  }
  .bf-col-sm-1-5 {
    width: 20%;
  }
  .bf-col-sm-2-5 {
    width: 40%;
  }
  .bf-col-sm-3-5 {
    width: 60%;
  }
  .bf-col-sm-4-5 {
    width: 80%;
  }
  .bf-col-sm-5-5 {
    width: 100%;
  }
  .bf-col-sm-1-6 {
    width: 16.6667%;
  }
  .bf-col-sm-2-6 {
    width: 33.3333%;
  }
  .bf-col-sm-3-6 {
    width: 50%;
  }
  .bf-col-sm-4-6 {
    width: 66.6667%;
  }
  .bf-col-sm-5-6 {
    width: 83.3333%;
  }
  .bf-col-sm-6-6 {
    width: 100%;
  }
  .bf-col-sm-1-8 {
    width: 12.5%;
  }
  .bf-col-sm-2-8 {
    width: 25%;
  }
  .bf-col-sm-3-8 {
    width: 37.5%;
  }
  .bf-col-sm-4-8 {
    width: 50%;
  }
  .bf-col-sm-5-8 {
    width: 62.5%;
  }
  .bf-col-sm-6-8 {
    width: 75%;
  }
  .bf-col-sm-7-8 {
    width: 87.5%;
  }
  .bf-col-sm-8-8 {
    width: 100%;
  }
  .bf-col-sm-1-12 {
    width: 8.3333%;
  }
  .bf-col-sm-2-12 {
    width: 16.6667%;
  }
  .bf-col-sm-3-12 {
    width: 25%;
  }
  .bf-col-sm-4-12 {
    width: 33.3333%;
  }
  .bf-col-sm-5-12 {
    width: 41.6667%;
  }
  .bf-col-sm-6-12 {
    width: 50%;
  }
  .bf-col-sm-7-12 {
    width: 58.3333%;
  }
  .bf-col-sm-8-12 {
    width: 66.6667%;
  }
  .bf-col-sm-9-12 {
    width: 75%;
  }
  .bf-col-sm-10-12 {
    width: 83.3333%;
  }
  .bf-col-sm-11-12 {
    width: 91.6667%;
  }
  .bf-col-sm-12-12 {
    width: 100%;
  }
  .bf-col-sm-1-24 {
    width: 4.1667%;
  }
  .bf-col-sm-2-24 {
    width: 8.3333%;
  }
  .bf-col-sm-3-24 {
    width: 12.5%;
  }
  .bf-col-sm-4-24 {
    width: 16.6667%;
  }
  .bf-col-sm-5-24 {
    width: 20.8333%;
  }
  .bf-col-sm-6-24 {
    width: 25%;
  }
  .bf-col-sm-7-24 {
    width: 29.1667%;
  }
  .bf-col-sm-8-24 {
    width: 33.3333%;
  }
  .bf-col-sm-9-24 {
    width: 37.5%;
  }
  .bf-col-sm-10-24 {
    width: 41.6667%;
  }
  .bf-col-sm-11-24 {
    width: 45.8333%;
  }
  .bf-col-sm-12-24 {
    width: 50%;
  }
  .bf-col-sm-13-24 {
    width: 54.1667%;
  }
  .bf-col-sm-14-24 {
    width: 58.3333%;
  }
  .bf-col-sm-15-24 {
    width: 62.5%;
  }
  .bf-col-sm-16-24 {
    width: 66.6667%;
  }
  .bf-col-sm-17-24 {
    width: 70.8333%;
  }
  .bf-col-sm-18-24 {
    width: 75%;
  }
  .bf-col-sm-19-24 {
    width: 79.1667%;
  }
  .bf-col-sm-20-24 {
    width: 83.3333%;
  }
  .bf-col-sm-21-24 {
    width: 87.5%;
  }
  .bf-col-sm-22-24 {
    width: 91.6667%;
  }
  .bf-col-sm-23-24 {
    width: 95.8333%;
  }
  .bf-col-sm-24-24 {
    width: 100%;
  }
  .hidden-sm {
    display: none !important;
  }
  .visible-sm-inline-block {
    display: inline-block !important;
  }
  .visible-sm-inline {
    display: inline !important;
  }
  .visible-sm-block {
    display: block !important;
  }
}
@media screen and (min-width: 80em) {
  .bf-col-md-1,
  .bf-col-md-1-1 {
    width: 100%;
  }
  .bf-col-md-1-2 {
    width: 50%;
  }
  .bf-col-md-2-2 {
    width: 100%;
  }
  .bf-col-md-1-3 {
    width: 33.3333%;
  }
  .bf-col-md-2-3 {
    width: 66.6667%;
  }
  .bf-col-md-3-3 {
    width: 100%;
  }
  .bf-col-md-1-4 {
    width: 25%;
  }
  .bf-col-md-2-4 {
    width: 50%;
  }
  .bf-col-md-3-4 {
    width: 75%;
  }
  .bf-col-md-4-4 {
    width: 100%;
  }
  .bf-col-md-1-5 {
    width: 20%;
  }
  .bf-col-md-2-5 {
    width: 40%;
  }
  .bf-col-md-3-5 {
    width: 60%;
  }
  .bf-col-md-4-5 {
    width: 80%;
  }
  .bf-col-md-5-5 {
    width: 100%;
  }
  .bf-col-md-1-6 {
    width: 16.6667%;
  }
  .bf-col-md-2-6 {
    width: 33.3333%;
  }
  .bf-col-md-3-6 {
    width: 50%;
  }
  .bf-col-md-4-6 {
    width: 66.6667%;
  }
  .bf-col-md-5-6 {
    width: 83.3333%;
  }
  .bf-col-md-6-6 {
    width: 100%;
  }
  .bf-col-md-1-8 {
    width: 12.5%;
  }
  .bf-col-md-2-8 {
    width: 25%;
  }
  .bf-col-md-3-8 {
    width: 37.5%;
  }
  .bf-col-md-4-8 {
    width: 50%;
  }
  .bf-col-md-5-8 {
    width: 62.5%;
  }
  .bf-col-md-6-8 {
    width: 75%;
  }
  .bf-col-md-7-8 {
    width: 87.5%;
  }
  .bf-col-md-8-8 {
    width: 100%;
  }
  .bf-col-md-1-12 {
    width: 8.3333%;
  }
  .bf-col-md-2-12 {
    width: 16.6667%;
  }
  .bf-col-md-3-12 {
    width: 25%;
  }
  .bf-col-md-4-12 {
    width: 33.3333%;
  }
  .bf-col-md-5-12 {
    width: 41.6667%;
  }
  .bf-col-md-6-12 {
    width: 50%;
  }
  .bf-col-md-7-12 {
    width: 58.3333%;
  }
  .bf-col-md-8-12 {
    width: 66.6667%;
  }
  .bf-col-md-9-12 {
    width: 75%;
  }
  .bf-col-md-10-12 {
    width: 83.3333%;
  }
  .bf-col-md-11-12 {
    width: 91.6667%;
  }
  .bf-col-md-12-12 {
    width: 100%;
  }
  .bf-col-md-1-24 {
    width: 4.1667%;
  }
  .bf-col-md-2-24 {
    width: 8.3333%;
  }
  .bf-col-md-3-24 {
    width: 12.5%;
  }
  .bf-col-md-4-24 {
    width: 16.6667%;
  }
  .bf-col-md-5-24 {
    width: 20.8333%;
  }
  .bf-col-md-6-24 {
    width: 25%;
  }
  .bf-col-md-7-24 {
    width: 29.1667%;
  }
  .bf-col-md-8-24 {
    width: 33.3333%;
  }
  .bf-col-md-9-24 {
    width: 37.5%;
  }
  .bf-col-md-10-24 {
    width: 41.6667%;
  }
  .bf-col-md-11-24 {
    width: 45.8333%;
  }
  .bf-col-md-12-24 {
    width: 50%;
  }
  .bf-col-md-13-24 {
    width: 54.1667%;
  }
  .bf-col-md-14-24 {
    width: 58.3333%;
  }
  .bf-col-md-15-24 {
    width: 62.5%;
  }
  .bf-col-md-16-24 {
    width: 66.6667%;
  }
  .bf-col-md-17-24 {
    width: 70.8333%;
  }
  .bf-col-md-18-24 {
    width: 75%;
  }
  .bf-col-md-19-24 {
    width: 79.1667%;
  }
  .bf-col-md-20-24 {
    width: 83.3333%;
  }
  .bf-col-md-21-24 {
    width: 87.5%;
  }
  .bf-col-md-22-24 {
    width: 91.6667%;
  }
  .bf-col-md-23-24 {
    width: 95.8333%;
  }
  .bf-col-md-24-24 {
    width: 100%;
  }
  .hidden-md {
    display: none !important;
  }
  .visible-md-inline-block {
    display: inline-block !important;
  }
  .visible-md-inline {
    display: inline !important;
  }
  .visible-md-block {
    display: block !important;
  }
}
@media screen and (min-width: 85.375em) {
  .bf-col-lg-1,
  .bf-col-lg-1-1 {
    width: 100%;
  }
  .bf-col-lg-1-2 {
    width: 50%;
  }
  .bf-col-lg-2-2 {
    width: 100%;
  }
  .bf-col-lg-1-3 {
    width: 33.3333%;
  }
  .bf-col-lg-2-3 {
    width: 66.6667%;
  }
  .bf-col-lg-3-3 {
    width: 100%;
  }
  .bf-col-lg-1-4 {
    width: 25%;
  }
  .bf-col-lg-2-4 {
    width: 50%;
  }
  .bf-col-lg-3-4 {
    width: 75%;
  }
  .bf-col-lg-4-4 {
    width: 100%;
  }
  .bf-col-lg-1-5 {
    width: 20%;
  }
  .bf-col-lg-2-5 {
    width: 40%;
  }
  .bf-col-lg-3-5 {
    width: 60%;
  }
  .bf-col-lg-4-5 {
    width: 80%;
  }
  .bf-col-lg-5-5 {
    width: 100%;
  }
  .bf-col-lg-1-6 {
    width: 16.6667%;
  }
  .bf-col-lg-2-6 {
    width: 33.3333%;
  }
  .bf-col-lg-3-6 {
    width: 50%;
  }
  .bf-col-lg-4-6 {
    width: 66.6667%;
  }
  .bf-col-lg-5-6 {
    width: 83.3333%;
  }
  .bf-col-lg-6-6 {
    width: 100%;
  }
  .bf-col-lg-1-8 {
    width: 12.5%;
  }
  .bf-col-lg-2-8 {
    width: 25%;
  }
  .bf-col-lg-3-8 {
    width: 37.5%;
  }
  .bf-col-lg-4-8 {
    width: 50%;
  }
  .bf-col-lg-5-8 {
    width: 62.5%;
  }
  .bf-col-lg-6-8 {
    width: 75%;
  }
  .bf-col-lg-7-8 {
    width: 87.5%;
  }
  .bf-col-lg-8-8 {
    width: 100%;
  }
  .bf-col-lg-1-12 {
    width: 8.3333%;
  }
  .bf-col-lg-2-12 {
    width: 16.6667%;
  }
  .bf-col-lg-3-12 {
    width: 25%;
  }
  .bf-col-lg-4-12 {
    width: 33.3333%;
  }
  .bf-col-lg-5-12 {
    width: 41.6667%;
  }
  .bf-col-lg-6-12 {
    width: 50%;
  }
  .bf-col-lg-7-12 {
    width: 58.3333%;
  }
  .bf-col-lg-8-12 {
    width: 66.6667%;
  }
  .bf-col-lg-9-12 {
    width: 75%;
  }
  .bf-col-lg-10-12 {
    width: 83.3333%;
  }
  .bf-col-lg-11-12 {
    width: 91.6667%;
  }
  .bf-col-lg-12-12 {
    width: 100%;
  }
  .bf-col-lg-1-24 {
    width: 4.1667%;
  }
  .bf-col-lg-2-24 {
    width: 8.3333%;
  }
  .bf-col-lg-3-24 {
    width: 12.5%;
  }
  .bf-col-lg-4-24 {
    width: 16.6667%;
  }
  .bf-col-lg-5-24 {
    width: 20.8333%;
  }
  .bf-col-lg-6-24 {
    width: 25%;
  }
  .bf-col-lg-7-24 {
    width: 29.1667%;
  }
  .bf-col-lg-8-24 {
    width: 33.3333%;
  }
  .bf-col-lg-9-24 {
    width: 37.5%;
  }
  .bf-col-lg-10-24 {
    width: 41.6667%;
  }
  .bf-col-lg-11-24 {
    width: 45.8333%;
  }
  .bf-col-lg-12-24 {
    width: 50%;
  }
  .bf-col-lg-13-24 {
    width: 54.1667%;
  }
  .bf-col-lg-14-24 {
    width: 58.3333%;
  }
  .bf-col-lg-15-24 {
    width: 62.5%;
  }
  .bf-col-lg-16-24 {
    width: 66.6667%;
  }
  .bf-col-lg-17-24 {
    width: 70.8333%;
  }
  .bf-col-lg-18-24 {
    width: 75%;
  }
  .bf-col-lg-19-24 {
    width: 79.1667%;
  }
  .bf-col-lg-20-24 {
    width: 83.3333%;
  }
  .bf-col-lg-21-24 {
    width: 87.5%;
  }
  .bf-col-lg-22-24 {
    width: 91.6667%;
  }
  .bf-col-lg-23-24 {
    width: 95.8333%;
  }
  .bf-col-lg-24-24 {
    width: 100%;
  }
  .hidden-lg {
    display: none !important;
  }
  .visible-lg-inline-block {
    display: inline-block !important;
  }
  .visible-lg-inline {
    display: inline !important;
  }
  .visible-lg-block {
    display: block !important;
  }
}
@media screen and (min-width: 90em) {
  .bf-col-xl-1,
  .bf-col-xl-1-1 {
    width: 100%;
  }
  .bf-col-xl-1-2 {
    width: 50%;
  }
  .bf-col-xl-2-2 {
    width: 100%;
  }
  .bf-col-xl-1-3 {
    width: 33.3333%;
  }
  .bf-col-xl-2-3 {
    width: 66.6667%;
  }
  .bf-col-xl-3-3 {
    width: 100%;
  }
  .bf-col-xl-1-4 {
    width: 25%;
  }
  .bf-col-xl-2-4 {
    width: 50%;
  }
  .bf-col-xl-3-4 {
    width: 75%;
  }
  .bf-col-xl-4-4 {
    width: 100%;
  }
  .bf-col-xl-1-5 {
    width: 20%;
  }
  .bf-col-xl-2-5 {
    width: 40%;
  }
  .bf-col-xl-3-5 {
    width: 60%;
  }
  .bf-col-xl-4-5 {
    width: 80%;
  }
  .bf-col-xl-5-5 {
    width: 100%;
  }
  .bf-col-xl-1-6 {
    width: 16.6667%;
  }
  .bf-col-xl-2-6 {
    width: 33.3333%;
  }
  .bf-col-xl-3-6 {
    width: 50%;
  }
  .bf-col-xl-4-6 {
    width: 66.6667%;
  }
  .bf-col-xl-5-6 {
    width: 83.3333%;
  }
  .bf-col-xl-6-6 {
    width: 100%;
  }
  .bf-col-xl-1-8 {
    width: 12.5%;
  }
  .bf-col-xl-2-8 {
    width: 25%;
  }
  .bf-col-xl-3-8 {
    width: 37.5%;
  }
  .bf-col-xl-4-8 {
    width: 50%;
  }
  .bf-col-xl-5-8 {
    width: 62.5%;
  }
  .bf-col-xl-6-8 {
    width: 75%;
  }
  .bf-col-xl-7-8 {
    width: 87.5%;
  }
  .bf-col-xl-8-8 {
    width: 100%;
  }
  .bf-col-xl-1-12 {
    width: 8.3333%;
  }
  .bf-col-xl-2-12 {
    width: 16.6667%;
  }
  .bf-col-xl-3-12 {
    width: 25%;
  }
  .bf-col-xl-4-12 {
    width: 33.3333%;
  }
  .bf-col-xl-5-12 {
    width: 41.6667%;
  }
  .bf-col-xl-6-12 {
    width: 50%;
  }
  .bf-col-xl-7-12 {
    width: 58.3333%;
  }
  .bf-col-xl-8-12 {
    width: 66.6667%;
  }
  .bf-col-xl-9-12 {
    width: 75%;
  }
  .bf-col-xl-10-12 {
    width: 83.3333%;
  }
  .bf-col-xl-11-12 {
    width: 91.6667%;
  }
  .bf-col-xl-12-12 {
    width: 100%;
  }
  .bf-col-xl-1-24 {
    width: 4.1667%;
  }
  .bf-col-xl-2-24 {
    width: 8.3333%;
  }
  .bf-col-xl-3-24 {
    width: 12.5%;
  }
  .bf-col-xl-4-24 {
    width: 16.6667%;
  }
  .bf-col-xl-5-24 {
    width: 20.8333%;
  }
  .bf-col-xl-6-24 {
    width: 25%;
  }
  .bf-col-xl-7-24 {
    width: 29.1667%;
  }
  .bf-col-xl-8-24 {
    width: 33.3333%;
  }
  .bf-col-xl-9-24 {
    width: 37.5%;
  }
  .bf-col-xl-10-24 {
    width: 41.6667%;
  }
  .bf-col-xl-11-24 {
    width: 45.8333%;
  }
  .bf-col-xl-12-24 {
    width: 50%;
  }
  .bf-col-xl-13-24 {
    width: 54.1667%;
  }
  .bf-col-xl-14-24 {
    width: 58.3333%;
  }
  .bf-col-xl-15-24 {
    width: 62.5%;
  }
  .bf-col-xl-16-24 {
    width: 66.6667%;
  }
  .bf-col-xl-17-24 {
    width: 70.8333%;
  }
  .bf-col-xl-18-24 {
    width: 75%;
  }
  .bf-col-xl-19-24 {
    width: 79.1667%;
  }
  .bf-col-xl-20-24 {
    width: 83.3333%;
  }
  .bf-col-xl-21-24 {
    width: 87.5%;
  }
  .bf-col-xl-22-24 {
    width: 91.6667%;
  }
  .bf-col-xl-23-24 {
    width: 95.8333%;
  }
  .bf-col-xl-24-24 {
    width: 100%;
  }
  .hidden-xl {
    display: none !important;
  }
  .visible-xl-inline-block {
    display: inline-block !important;
  }
  .visible-xl-inline {
    display: inline !important;
  }
  .visible-xl-block {
    display: block !important;
  }
}
@media screen and (min-width: 100em) {
  .bf-col-xxl-1,
  .bf-col-xxl-1-1 {
    width: 100%;
  }
  .bf-col-xxl-1-2 {
    width: 50%;
  }
  .bf-col-xxl-2-2 {
    width: 100%;
  }
  .bf-col-xxl-1-3 {
    width: 33.3333%;
  }
  .bf-col-xxl-2-3 {
    width: 66.6667%;
  }
  .bf-col-xxl-3-3 {
    width: 100%;
  }
  .bf-col-xxl-1-4 {
    width: 25%;
  }
  .bf-col-xxl-2-4 {
    width: 50%;
  }
  .bf-col-xxl-3-4 {
    width: 75%;
  }
  .bf-col-xxl-4-4 {
    width: 100%;
  }
  .bf-col-xxl-1-5 {
    width: 20%;
  }
  .bf-col-xxl-2-5 {
    width: 40%;
  }
  .bf-col-xxl-3-5 {
    width: 60%;
  }
  .bf-col-xxl-4-5 {
    width: 80%;
  }
  .bf-col-xxl-5-5 {
    width: 100%;
  }
  .bf-col-xxl-1-6 {
    width: 16.6667%;
  }
  .bf-col-xxl-2-6 {
    width: 33.3333%;
  }
  .bf-col-xxl-3-6 {
    width: 50%;
  }
  .bf-col-xxl-4-6 {
    width: 66.6667%;
  }
  .bf-col-xxl-5-6 {
    width: 83.3333%;
  }
  .bf-col-xxl-6-6 {
    width: 100%;
  }
  .bf-col-xxl-1-8 {
    width: 12.5%;
  }
  .bf-col-xxl-2-8 {
    width: 25%;
  }
  .bf-col-xxl-3-8 {
    width: 37.5%;
  }
  .bf-col-xxl-4-8 {
    width: 50%;
  }
  .bf-col-xxl-5-8 {
    width: 62.5%;
  }
  .bf-col-xxl-6-8 {
    width: 75%;
  }
  .bf-col-xxl-7-8 {
    width: 87.5%;
  }
  .bf-col-xxl-8-8 {
    width: 100%;
  }
  .bf-col-xxl-1-12 {
    width: 8.3333%;
  }
  .bf-col-xxl-2-12 {
    width: 16.6667%;
  }
  .bf-col-xxl-3-12 {
    width: 25%;
  }
  .bf-col-xxl-4-12 {
    width: 33.3333%;
  }
  .bf-col-xxl-5-12 {
    width: 41.6667%;
  }
  .bf-col-xxl-6-12 {
    width: 50%;
  }
  .bf-col-xxl-7-12 {
    width: 58.3333%;
  }
  .bf-col-xxl-8-12 {
    width: 66.6667%;
  }
  .bf-col-xxl-9-12 {
    width: 75%;
  }
  .bf-col-xxl-10-12 {
    width: 83.3333%;
  }
  .bf-col-xxl-11-12 {
    width: 91.6667%;
  }
  .bf-col-xxl-12-12 {
    width: 100%;
  }
  .bf-col-xxl-1-24 {
    width: 4.1667%;
  }
  .bf-col-xxl-2-24 {
    width: 8.3333%;
  }
  .bf-col-xxl-3-24 {
    width: 12.5%;
  }
  .bf-col-xxl-4-24 {
    width: 16.6667%;
  }
  .bf-col-xxl-5-24 {
    width: 20.8333%;
  }
  .bf-col-xxl-6-24 {
    width: 25%;
  }
  .bf-col-xxl-7-24 {
    width: 29.1667%;
  }
  .bf-col-xxl-8-24 {
    width: 33.3333%;
  }
  .bf-col-xxl-9-24 {
    width: 37.5%;
  }
  .bf-col-xxl-10-24 {
    width: 41.6667%;
  }
  .bf-col-xxl-11-24 {
    width: 45.8333%;
  }
  .bf-col-xxl-12-24 {
    width: 50%;
  }
  .bf-col-xxl-13-24 {
    width: 54.1667%;
  }
  .bf-col-xxl-14-24 {
    width: 58.3333%;
  }
  .bf-col-xxl-15-24 {
    width: 62.5%;
  }
  .bf-col-xxl-16-24 {
    width: 66.6667%;
  }
  .bf-col-xxl-17-24 {
    width: 70.8333%;
  }
  .bf-col-xxl-18-24 {
    width: 75%;
  }
  .bf-col-xxl-19-24 {
    width: 79.1667%;
  }
  .bf-col-xxl-20-24 {
    width: 83.3333%;
  }
  .bf-col-xxl-21-24 {
    width: 87.5%;
  }
  .bf-col-xxl-22-24 {
    width: 91.6667%;
  }
  .bf-col-xxl-23-24 {
    width: 95.8333%;
  }
  .bf-col-xxl-24-24 {
    width: 100%;
  }
  .hidden-xxl {
    display: none !important;
  }
  .visible-xxl-inline-block {
    display: inline-block !important;
  }
  .visible-xxl-inline {
    display: inline !important;
  }
  .visible-xxl-block {
    display: block !important;
  }
}
.visible-inline-block {
  display: inline-block !important;
}
.visible-inline {
  display: inline !important;
}
.visible-block {
  display: block !important;
}
@media screen and (orientation: portrait) {
  .visible-portrait {
    display: block !important;
  }
}
@media screen and (orientation: landscape) {
  .visible-landscape {
    display: block !important;
  }
}
.no-bottom-gutter {
  margin-bottom: 0;
}
.no-side-gutter [class*="bf-col-"]:not(:first-child):not(:last-child) {
  padding-left: 0;
  padding-right: 0;
}
.no-side-gutter [class*="bf-col-"]:first-child {
  padding-right: 0;
}
.no-side-gutter [class*="bf-col-"]:last-child {
  padding-left: 0;
}
.bf-btn {
  display: inline-block;
  cursor: pointer;
  text-align: center;
  vertical-align: middle;
  white-space: nowrap;
  text-decoration: none;
  color: #333;
  border: 1px solid transparent;
  background-color: #eee;
  font-size: 12px;
  line-height: 20px;
  padding: 6px 12px;
  border-radius: 3px;
}
.bf-btn:hover {
  background-color: #e1e1e1;
}
.bf-btn-xs {
  font-size: 9px;
  line-height: 10px;
  padding: 2px 4px;
  border-radius: 2px;
}
.bf-btn-sm {
  font-size: 12px;
  line-height: 20px;
  padding: 3px 6px;
  border-radius: 2px;
}
.bf-btn-lg {
  font-size: 14px;
  line-height: 20px;
  padding: 9px 18px;
  border-radius: 4px;
}
.bf-btn-xl {
  font-size: 17px;
  line-height: 20px;
  padding: 15px 30px;
  border-radius: 5px;
}
.mv-bet-button,
.mv-header-container {
  font-family: Tahoma, Verdana, Arial, sans-serif;
  font-size: 11px;
}
.mv-header-container .cashout-availability .cashout-label,
.mv-header-container .market-status .market-status-label {
  margin-left: 5px;
}
@keyframes highlightBack {
  0%,
  100% {
    background-color: #a6d8ff;
  }
  50% {
    background-color: #ff0;
  }
}
@keyframes highlightLay {
  0%,
  100% {
    background-color: #fac9d1;
  }
  50% {
    background-color: #ff0;
  }
}
@keyframes highlightDefault {
  0%,
  100% {
    background-color: #fff;
  }
  50% {
    background-color: #ff0;
  }
}
.mv-bet-button {
  width: 100%;
  height: 100%;
  border-width: 0;
  background-color: #fff;
  outline: 0;
  cursor: pointer;
}
.mv-bet-button.changed {
  -webkit-animation-name: highlightDefault;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: highlightDefault;
  -moz-animation-duration: 0.3s;
  animation-name: highlightDefault;
  animation-duration: 0.3s;
}
.mv-bet-button.selected {
  box-shadow: inset 0 0 6px 0 rgba(127, 127, 127, 0.8);
}
.mv-bet-button.selected.back-button.is-sp,
.mv-bet-button.selected.back-selection-button {
  background-color: #75c2fd;
}
.mv-bet-button.selected.lay-button.is-sp,
.mv-bet-button.selected.lay-selection-button {
  background-color: #f694aa;
}
.mv-bet-button:hover {
  background-color: #dfdfdf;
}
.mv-bet-button .bet-button-price,
.mv-bet-button .bet-button-size,
.mv-bet-button .sp-label {
  text-align: center;
  display: block;
}
.mv-bet-button .bet-button-price,
.mv-bet-button .sp-label {
  font-weight: 700;
}
.mv-bet-button.back-button.is-sp,
.mv-bet-button.back-selection-button {
  background-color: #a6d8ff;
}
.mv-bet-button.back-button.is-sp:hover,
.mv-bet-button.back-selection-button:hover {
  background-color: #75c2fd;
}
.mv-bet-button.lay-button.is-sp,
.mv-bet-button.lay-selection-button {
  background-color: #fac9d1;
}
.mv-bet-button.lay-button.is-sp:hover,
.mv-bet-button.lay-selection-button:hover {
  background-color: #f694aa;
}
.mv-header-container:after {
  content: "";
  clear: both;
  display: block;
}
.mv-header-container .mv-header-field {
  line-height: 16px;
  display: inline-block;
  padding-top: 2px;
  padding-bottom: 2px;
  margin-right: 8px;
  vertical-align: middle;
}
.mv-header-container .checkbox-with-label {
  text-align: left;
}
.mv-header-container .market-name {
  color: #1e1e1e;
  font-size: 12px;
  font-weight: 700;
  padding-left: 8px;
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
}
.mv-header-container .market-matched {
  white-space: nowrap;
}
.mv-header-container .market-status {
  height: 16px;
}
.mv-header-container .market-status .market-status-icon {
  width: 16px;
  height: 16px;
  float: left;
  background-color: #fff;
}
.mv-header-container .market-status.market-inplay {
  color: #090;
}
.mv-header-container .market-status.market-inplay .market-status-icon {
  background-color: #090;
}
.mv-header-container .market-status.market-going-inplay {
  color: #273a47;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.mv-header-container .market-status.market-going-inplay .market-status-icon {
  background-color: #7f7f7f;
}
.mv-header-container .market-status.market-closed {
  color: #b30000;
}
.mv-header-container .market-status.market-closed .market-status-icon {
  display: none;
}
.mv-header-container .cashout-availability .cashout-icon {
  width: 16px;
  height: 16px;
  float: left;
  background-color: #ffb900;
}
@media only screen and (max-width: 1279px) {
  .mv-header-container .cashout-availability .cashout-label {
    display: none;
  }
}
.mv-header-container .bsp-preferences .bsp-tooltip-icon {
  margin-left: 3px;
  width: 13px;
  height: 13px;
}
.mv-header-container .bsp-preferences .bsp-tooltip-icon .bsp-tooltip-link {
  cursor: help;
  color: #2789ce;
}
.mv-header-container .market-rules .market-rules-icon {
  width: 16px;
  height: 16px;
  float: left;
  background-color: #595959;
  cursor: pointer;
}
.mv-header-container .market-rules .market-rules-link {
  display: inline-block;
  text-decoration: none;
  color: #1e1e1e;
  cursor: pointer;
}
.mv-header-container .market-rules .market-rules-label {
  display: inline-block;
  background-color: #bfbfbf;
  color: #1e1e1e;
  padding: 0 5px;
  border-radius: 0 2px 2px 0;
  -moz-border-radius: 0 2px 2px 0;
  -webkit-border-radius: 0 2px 2px 0;
  border-left: 1px solid #7f7f7f;
}
.mv-header-container .total-matched,
.mv-header-container .total-matched-label {
  font-family: Tahoma, Verdana, Arial, sans-serif;
  font-size: 11px;
  color: #273a47;
  white-space: nowrap;
}
.mv-header-container .pin-runners,
.mv-header-container .refresh-btn {
  color: #1e1e1e;
  line-height: 16px;
  font-family: Tahoma, Verdana, Arial, sans-serif;
  font-size: 11px;
}
.mv-header-container .total-matched-label {
  padding: 3px;
}
.mv-header-container .total-matched {
  font-weight: 700;
  margin-right: 5px;
}
.mv-header-container .refresh-btn {
  border: 0;
  background-color: #bfbfbf;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  padding: 0 10px;
  margin: 0;
  cursor: pointer;
}
.mv-header-container .refresh-btn:active {
  box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.25);
}
.mv-header-container .refresh-btn:focus {
  outline: 0;
}
.mv-header-container .refresh-btn:hover {
  cursor: pointer;
  background-color: #acacac;
}
.mv-header-container .pin-runners {
  height: 16px;
  background-color: #dfdfdf;
  text-align: center;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
}
.mv-header-container .pin-runners label {
  cursor: pointer;
}
.mv-header-container .pin-runners.active {
  background-color: #c2c2c2;
}
.mv-header-container .pin-runners .pin-runners-icon {
  margin-left: 3px;
  width: 16px;
  height: 16px;
  float: left;
  background-color: #595959;
}
.mv-header-container .pin-runners .pin-runners-checkbox {
  display: none;
}
.mv-header-container .pin-runners .pin-runners-label {
  padding: 0 6px 0 3px;
  line-height: 16px;
  display: inline-block;
}
.mv-header-container.marketview .mv-header-content {
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
.mv-header-container.marketview
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
.mv-header-container.marketview .mv-secondary-section {
  -ms-flex-item-align: start;
  align-self: flex-start;
  -ms-flex: none;
  flex: none;
}
.mv-header-container.marketview .market-matched,
.mv-header-container.marketview .mv-header-total-matched-wrapper {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-flow: row nowrap;
  flex-flow: row nowrap;
  -ms-flex-align: center;
  align-items: center;
}
.ie10 .mv-header-container.marketview .mv-header-content,
.ie11 .mv-header-container.marketview .mv-header-content,
.ie9 .mv-header-container.marketview .mv-header-content {
  display: table;
  width: 100%;
}
.ie10 .mv-header-container.marketview .mv-header-main-section-wrapper,
.ie11 .mv-header-container.marketview .mv-header-main-section-wrapper,
.ie9 .mv-header-container.marketview .mv-header-main-section-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.ie10 .mv-header-container.marketview .mv-secondary-section,
.ie11 .mv-header-container.marketview .mv-secondary-section,
.ie9 .mv-header-container.marketview .mv-secondary-section {
  display: table-cell;
  float: right;
  padding: 2px;
}
.ie10 .mv-header-container.marketview .mv-header-total-matched-wrapper,
.ie11 .mv-header-container.marketview .mv-header-total-matched-wrapper,
.ie9 .mv-header-container.marketview .mv-header-total-matched-wrapper {
  display: table;
}
.ie10 .mv-header-container.marketview .market-matched,
.ie10 .mv-header-container.marketview .refresh-btn,
.ie11 .mv-header-container.marketview .market-matched,
.ie11 .mv-header-container.marketview .refresh-btn,
.ie9 .mv-header-container.marketview .market-matched,
.ie9 .mv-header-container.marketview .refresh-btn {
  display: table-cell;
}
.mv-header-container.mini-marketview .mv-header-main-section-wrapper {
  background: #ebebeb;
  border-bottom: 1px solid #dfdfdf;
  width: 100%;
  min-height: 28px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-flow: row nowrap;
  flex-flow: row nowrap;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: justify;
  justify-content: space-between;
  overflow: auto;
}
.mv-header-container.mini-marketview .mv-header-main-section {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-flow: row wrap;
  flex-flow: row wrap;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: end;
  justify-content: flex-end;
  padding: 5px 0 5px 8px;
  -ms-flex: 1 0 auto;
  flex: 1 0 auto;
}
.mv-header-container.mini-marketview .mv-secondary-section {
  float: left;
  margin-top: 8px;
}
.mv-header-container.mini-marketview .mv-header-total-matched-wrapper {
  margin-left: 6px;
}
.mv-header-container.mini-marketview .total-matched,
.mv-header-container.mini-marketview .total-matched-label {
  color: #7f7f7f;
  font-weight: 400;
}
.ie10 .mv-header-container.mini-marketview .mv-header-main-section-wrapper,
.ie11 .mv-header-container.mini-marketview .mv-header-main-section-wrapper,
.ie9 .mv-header-container.mini-marketview .mv-header-main-section-wrapper {
  display: table;
}
.ie10 .mv-header-container.mini-marketview .mv-header-main-section,
.ie11 .mv-header-container.mini-marketview .mv-header-main-section,
.ie9 .mv-header-container.mini-marketview .mv-header-main-section {
  display: table-cell;
  vertical-align: middle;
  text-align: right;
}
.ie10 .mv-header-container.mini-marketview .market-name,
.ie11 .mv-header-container.mini-marketview .market-name,
.ie9 .mv-header-container.mini-marketview .market-name {
  display: table-cell;
  vertical-align: middle;
  float: none;
}
.runner-metadata-list {
  box-shadow: 0 0 3px 0 #3b5160;
  font-size: 11px;
  font-weight: 400;
  list-style: none;
  background: #fff;
  color: #3b5160;
  cursor: default;
  line-height: 120%;
  z-index: 10;
  border: 1px solid #e0e6e6;
  position: absolute;
  padding: 3px;
  margin: 0;
  left: 0;
  top: 0;
  white-space: nowrap;
  visibility: hidden;
}
.runner-metadata-list.visible {
  display: block;
  visibility: visible;
}
.runner-info {
  font-size: 11px;
  padding-right: 5px;
}
.runner-info .name,
.runner-info .runner-numbers,
.runner-info .runner-silk {
  float: left;
}
.runner-info .runner-numbers {
  width: 25px;
}
.runner-info .runner-numbers p {
  line-height: 28px;
}
.runner-info .runner-numbers.double > p {
  line-height: 14px;
}
.runner-info .saddle-cloth,
.runner-info .stall-draw {
  color: #3b5160;
  height: 12px;
  text-align: center;
  margin: 0;
}
.runner-info .runner-silk {
  overflow: hidden;
  padding-top: 6px;
}
.runner-info .runner-silk .saddle-cloth-alpha {
  width: 25px;
  height: 20px;
  background: red;
}
.runner-info .runner-silk .horse-racing-silk {
  width: 26px;
  height: 21px;
}
.runner-info .runner-silk .greyhound-silk {
  width: 17px;
  height: 18px;
  background: red;
  margin: 0 3px;
}
.runner-info .horse-racing .jockey-name,
.runner-info .runner-name {
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  overflow: hidden;
  margin: 0;
  white-space: nowrap;
}
.runner-info .runner-name {
  font-weight: 700;
  line-height: 26px;
  padding: 2px 5px 1px;
}
.runner-info .horse-racing .jockey-name,
.runner-info .horse-racing .runner-name-with-jockey {
  line-height: 12px;
}
.runner-info .horse-racing .jockey-name {
  font-weight: 400;
  padding: 0 5px 2px;
}
.market-graph {
  border: 0;
}
.runner-elem-pnl {
  font-family: Tahoma, Verdana, Arial, sans-serif;
  font-size: 11px;
  float: left;
  color: #273a47;
  margin-right: 5px;
  white-space: nowrap;
}
.runner-elem-pnl .positive {
  color: #060;
}
.runner-elem-pnl .negative {
  color: #b30000;
}
.runner-elem-pnl .hidden {
  display: none;
}
.mod-tabs .more-dropdown .more-tab-item:not(:last-child),
.mod-tabs .tabs-container {
  border-bottom: 1px solid #dfdfdf;
}
.mod-tabs .tabs-container {
  font: 12px Arial, Helvetica, sans-serif;
  color: #1e1e1e;
  list-style-type: none;
  padding: 0;
  width: 100%;
  background-color: #efefef;
}
.mod-tabs .tab-container.more .more-tab-text,
.mod-tabs .tab-label {
  font-weight: 700;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
.mod-tabs .more-dropdown .more-tab-item .item-link,
.mod-tabs .tab-heading {
  text-decoration: none;
  color: inherit;
}
.mod-tabs .tab-container {
  display: inline-block;
  background-color: #efefef;
  text-align: center;
  cursor: pointer;
  vertical-align: middle;
  height: 100%;
  border-right: 1px solid #dfdfdf;
}
.mod-tabs .tab-container:focus,
.mod-tabs .tab-container:hover {
  background-color: #e4e4e4;
}
.mod-tabs .tab-container.more {
  position: relative;
  line-height: 12px;
}
.mod-tabs .tab-container.more .more-tab-selected {
  display: inline;
}
.mod-tabs .tab-container.more .more-icon {
  width: 9px;
  height: 6px;
  fill: #999;
  display: inline-block;
  margin-left: 4px;
}
.mod-tabs .tab-container.more .more-icon.with-thumbnail {
  vertical-align: bottom;
  margin-left: 0;
}
.mod-tabs .tab-container.more .tab-label {
  max-width: 80%;
  display: inline-block;
  vertical-align: top;
}
.mod-tabs .tab-container.more .tab-label.with-thumbnail {
  max-width: 100%;
}
.mod-tabs .tab-container.more .more-tab-text {
  max-width: 80%;
  display: inline-block;
  line-height: 100%;
  vertical-align: middle;
}
.mod-tabs .tab-container.more .tab-thumbnail-wrapper {
  width: 100%;
}
.mod-tabs .tab-container.active {
  border-top: 2px solid #ffb80c;
  background-color: #fff;
}
.mod-tabs .tab-heading {
  margin: 0;
  display: block;
  padding: 1px 16px;
  position: relative;
  top: 50%;
  transform: translateY(-50%);
}
.mod-tabs .tab-label {
  margin: 0 auto;
}
.mod-tabs .tab-label.with-thumbnail {
  line-height: 100%;
}
.mod-tabs .tab-thumbnail {
  vertical-align: text-top;
}
.mod-tabs .tab-thumbnail-wrapper {
  margin: 0 auto;
}
.mod-tabs .tab-thumbnail-wrapper.with-label {
  margin: 0 auto 4px;
}
.mod-tabs .more-dropdown {
  list-style-type: none;
  padding: 0;
  margin: 0;
  width: 100%;
  position: absolute;
  left: 0;
  background-color: #fff;
  text-align: left;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.3);
}
.mod-tabs .more-dropdown .more-tab-item {
  padding: 0 8px;
  line-height: 0;
}
.mod-tabs .more-dropdown .more-tab-item:hover {
  background-color: #e4e4e4;
}
.mod-tabs .more-dropdown .more-thumbnail-wrapper {
  display: inline-block;
  max-width: 20px;
  vertical-align: middle;
  margin: 8px 4px 8px 0;
  line-height: 0;
}
.mod-tabs .more-dropdown .more-tab-label {
  font: 12px Arial, Helvetica, sans-serif;
  margin: 0;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  line-height: 29px;
  display: inline-block;
  max-width: calc(100% - 24px);
  vertical-align: middle;
}
.mod-tabs .more-dropdown .more-tab-label.without-thumbnail {
  max-width: 100%;
}
.mod-inline-betting {
  outline: 0;
  font: 11px Arial, Helvetica, sans-serif;
}
.mod-inline-betting * {
  font-family: inherit;
  font-size: inherit;
  outline: 0;
}
.mod-inline-betting .place-bet-panel {
  color: #1e1e1e;
  background: #d2ebff;
  overflow: hidden;
  padding: 8px;
}
.mod-inline-betting .place-bet-panel .place-bet-container {
  overflow: auto;
}
.mod-inline-betting .place-bet-panel .bonus-container {
  width: 100%;
  height: 32px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -ms-flex-align: center;
  align-items: center;
  line-height: 0;
  margin-bottom: 8px;
}
.mod-inline-betting .place-bet-panel .bonus-info {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}
.mod-inline-betting .place-bet-panel .bonus-icon {
  padding: 2px;
  background-color: #2797e6;
  border-radius: 4px;
  margin-right: 4px;
}
.mod-inline-betting .place-bet-panel .bet-actions-container,
.mod-inline-betting .place-bet-panel .bet-info {
  display: inline-block;
}
.mod-inline-betting .place-bet-panel .bet-info {
  line-height: 14px;
}
.mod-inline-betting .place-bet-panel .bet-info-back,
.mod-inline-betting .place-bet-panel .bet-info-description,
.mod-inline-betting .place-bet-panel .bet-info-lay {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.mod-inline-betting .place-bet-panel .bet-info-description {
  font-weight: 700;
}
.mod-inline-betting .place-bet-panel.lay {
  background: #f3dce2;
}
.mod-inline-betting .place-bet-panel .inplay-bet-options-container,
.mod-inline-betting .place-bet-panel .pnl-info-container {
  display: none;
}
.mod-inline-betting .place-bet-panel.small .bet-info {
  max-width: 110px;
}
.mod-inline-betting .place-bet-panel.medium .bet-info {
  max-width: 170px;
}
.mod-inline-betting .place-bet-panel.large .bet-info {
  max-width: 230px;
}
.mod-inline-betting .place-bet-panel.extra-large .bet-info {
  max-width: 290px;
}
.mod-inline-betting .place-bet-panel.extra-small .bet-info {
  display: none;
}
.mod-inline-betting .place-bet-panel.extra-small .bet-actions-container {
  display: block;
  margin: auto;
  float: none;
  width: 100%;
}
.mod-inline-betting .place-bet-panel.back .bet-info-lay,
.mod-inline-betting .place-bet-panel.lay .bet-info-back {
  display: none;
}
.mod-inline-betting .confirm-bet-profit,
.mod-inline-betting .confirm-bet-title,
.mod-inline-betting .edit-bet,
.mod-inline-betting .place-bet-profit,
.mod-inline-betting .place-bet-title,
.mod-inline-betting .reset-bet {
  display: block;
  line-height: 11px;
  margin-top: 1px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.mod-inline-betting .confirm-bet-profit,
.mod-inline-betting .place-bet-profit {
  line-height: 9px;
  font-size: 9px;
  font-weight: 400;
}
.mod-inline-betting .cancel-notification,
.mod-inline-betting .confirm-bet,
.mod-inline-betting .edit-bet,
.mod-inline-betting .edit-notification,
.mod-inline-betting .place-bet,
.mod-inline-betting .price-input,
.mod-inline-betting .reset-bet,
.mod-inline-betting .size-input {
  box-sizing: border-box;
  height: 30px;
  margin-right: 4px;
  padding: 0;
  border: 0;
  border-radius: 2px;
  text-align: center;
  font-weight: 700;
  color: #1e1e1e;
  float: left;
}
.mod-inline-betting .price-container,
.mod-inline-betting .size-container {
  width: 78px;
  box-sizing: border-box;
  margin-right: 4px;
  float: left;
  height: 30px;
}
.mod-inline-betting .price-to-confirm,
.mod-inline-betting .size-to-confirm {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
  height: 100%;
}
.mod-inline-betting .price-to-confirm .price-label,
.mod-inline-betting .price-to-confirm .size-label,
.mod-inline-betting .size-to-confirm .price-label,
.mod-inline-betting .size-to-confirm .size-label {
  overflow: hidden;
  text-overflow: ellipsis;
}
.mod-inline-betting .price-to-confirm .price-value,
.mod-inline-betting .price-to-confirm .size-value,
.mod-inline-betting .size-to-confirm .price-value,
.mod-inline-betting .size-to-confirm .size-value {
  font-weight: 700;
}
.mod-inline-betting .negative-nudge,
.mod-inline-betting .positive-nudge {
  display: none;
}
.mod-inline-betting .separator {
  width: 1px;
  height: 30px;
  float: left;
  margin-left: -3px;
  margin-right: 2px;
  background-color: #85adcc;
}
.mod-inline-betting .lay .separator {
  background-color: #e1b4bb;
}
.mod-inline-betting .price-input,
.mod-inline-betting .size-input {
  width: 100%;
  background: #fff;
  -moz-appearance: textfield;
}
.mod-inline-betting .price-input::-webkit-inner-spin-button,
.mod-inline-betting .price-input::-webkit-outer-spin-button,
.mod-inline-betting .size-input::-webkit-inner-spin-button,
.mod-inline-betting .size-input::-webkit-outer-spin-button {
  -webkit-appearance: none;
}
.mod-inline-betting .price-input:disabled,
.mod-inline-betting .size-input:disabled {
  margin: 0;
  color: #a8a8a8;
}
.mod-inline-betting .edit-bet,
.mod-inline-betting .reset-bet {
  width: 120px;
  background: #bfbfbf;
  padding: 0 4px;
  cursor: pointer;
}
.mod-inline-betting .confirm-bet,
.mod-inline-betting .place-bet {
  width: 150px;
  padding: 0 4px;
  cursor: pointer;
  margin-right: 0;
  background: #ffb80c;
}
.mod-inline-betting .confirm-bet:disabled,
.mod-inline-betting .place-bet:disabled {
  cursor: not-allowed;
  color: #a8915b;
  background-color: #ffdc86;
}
.mod-inline-betting .liability-view-options-container {
  text-align: right;
}
.mod-inline-betting .liability-view-options-container label {
  display: inline-block;
  padding: 0 0 6px 6px;
}
.mod-inline-betting .liability-view-options-container label:first-child {
  padding-right: 6px;
}
.mod-inline-betting
  .liability-view-options-container
  label
  input[type="radio"] {
  vertical-align: middle;
  margin: -3px 2px 0 0;
}
.mod-inline-betting .bet-actions-container {
  float: right;
  overflow: auto;
  max-width: 438px;
}
.mod-inline-betting .notification-panel {
  padding: 8px 0 8px 8px;
}
.mod-inline-betting .notification-panel .message-container {
  margin: -3px 0;
}
.mod-inline-betting .loading-panel,
.mod-inline-betting .notification-panel {
  min-height: 30px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}
.mod-inline-betting .loading-panel .message-container,
.mod-inline-betting .notification-panel .message-container {
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
.mod-inline-betting .loading-panel .text-container,
.mod-inline-betting .notification-panel .text-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  -ms-flex-align: stretch;
  align-items: stretch;
  -ms-flex-item-align: center;
  align-self: center;
}
.mod-inline-betting .loading-panel .button-container,
.mod-inline-betting .notification-panel .button-container {
  -ms-flex: 0 0 auto;
  flex: 0 0 auto;
  margin-right: 8px;
}
.mod-inline-betting .loading-panel.dynamic-success,
.mod-inline-betting .loading-panel.success,
.mod-inline-betting .notification-panel.dynamic-success,
.mod-inline-betting .notification-panel.success {
  background: #20a052;
}
.mod-inline-betting .loading-panel.cancelled,
.mod-inline-betting .loading-panel.warning,
.mod-inline-betting .notification-panel.cancelled,
.mod-inline-betting .notification-panel.warning {
  background: #fff8d6;
}
.mod-inline-betting .loading-panel.cancelled .message,
.mod-inline-betting .loading-panel.cancelled .title,
.mod-inline-betting .loading-panel.warning .message,
.mod-inline-betting .loading-panel.warning .title,
.mod-inline-betting .notification-panel.cancelled .message,
.mod-inline-betting .notification-panel.cancelled .title,
.mod-inline-betting .notification-panel.warning .message,
.mod-inline-betting .notification-panel.warning .title {
  color: #1e1e1e;
}
.mod-inline-betting .loading-panel.cancelled .close-icon,
.mod-inline-betting .loading-panel.warning .close-icon,
.mod-inline-betting .notification-panel.cancelled .close-icon,
.mod-inline-betting .notification-panel.warning .close-icon {
  fill: #1e1e1e;
}
.mod-inline-betting .loading-panel.error,
.mod-inline-betting .notification-panel.error {
  background: #d54d4d;
}
.mod-inline-betting .loading-panel.error .cancel-notification,
.mod-inline-betting .loading-panel.error .edit-notification,
.mod-inline-betting .notification-panel.error .cancel-notification,
.mod-inline-betting .notification-panel.error .edit-notification {
  color: #d54d4d;
}
.mod-inline-betting .loading-panel.cancelled,
.mod-inline-betting .notification-panel.cancelled {
  background: #dfdfdf;
}
.mod-inline-betting .loading-panel .title,
.mod-inline-betting .notification-panel .title {
  font-weight: 700;
}
.mod-inline-betting .loading-panel .message,
.mod-inline-betting .loading-panel .reference,
.mod-inline-betting .loading-panel .title,
.mod-inline-betting .notification-panel .message,
.mod-inline-betting .notification-panel .reference,
.mod-inline-betting .notification-panel .title {
  color: #fff;
}
.mod-inline-betting .loading-panel .message,
.mod-inline-betting .notification-panel .message {
  white-space: pre-wrap;
}
.mod-inline-betting .loading-panel .reference,
.mod-inline-betting .notification-panel .reference {
  padding-top: 4px;
}
.mod-inline-betting .loading-panel .cancel-notification,
.mod-inline-betting .loading-panel .edit-notification,
.mod-inline-betting .notification-panel .cancel-notification,
.mod-inline-betting .notification-panel .edit-notification {
  background: #fff;
  padding: 0 8px;
  margin: 0 0 0 4px;
  cursor: pointer;
}
.mod-inline-betting .loading-panel .cancel-notification:disabled,
.mod-inline-betting .loading-panel .edit-notification:disabled,
.mod-inline-betting .notification-panel .cancel-notification:disabled,
.mod-inline-betting .notification-panel .edit-notification:disabled {
  cursor: not-allowed;
  color: #a9a9a9;
  background-color: #fff;
}
.mod-inline-betting .loading-panel .close-notification,
.mod-inline-betting .notification-panel .close-notification {
  cursor: pointer;
  width: 34px;
  height: 30px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: end;
  justify-content: flex-end;
  -ms-flex-align: center;
  align-items: center;
}
.mod-inline-betting .loading-panel .close-icon,
.mod-inline-betting .notification-panel .close-icon {
  width: 8px;
  height: 8px;
  fill: #fff;
  opacity: 0.5;
}
.mod-inline-betting .loading-panel {
  background: #efefef;
  height: 46px;
  position: relative;
  z-index: 2;
}
.mod-inline-betting .loading-panel .message,
.mod-inline-betting .loading-panel .title {
  color: #1e1e1e;
}
.mod-inline-betting .loading-panel .title {
  font-weight: 400;
}
.mod-inline-betting .loading-panel .message {
  font-weight: 700;
}
.mod-inline-betting .loading-panel .message-container {
  display: block;
  padding-left: 8px;
  z-index: 3;
}
.mod-inline-betting .loading-panel .progress-bar-container {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  z-index: -1;
}
.mod-inline-betting .loading-panel .progress-bar-container .progress-bar {
  background-color: #dfdfdf;
  height: 46px;
}
.mod-inline-betting .visible-when-narrow,
.mod-inline-betting.narrow .not-visible-when-narrow {
  display: none;
}
.mod-inline-betting.narrow .visible-when-narrow {
  display: block;
}
.mod-inline-betting.narrow .bet-info {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  line-height: normal;
  margin-bottom: 10px;
  width: 100%;
}
.mod-inline-betting.narrow .place-bet-panel.extra-small .bet-info {
  display: -ms-flexbox;
  display: flex;
  width: 100%;
}
.mod-inline-betting.narrow .bet-info .info {
  display: -ms-flexbox;
  display: flex;
}
.mod-inline-betting.narrow .bet-info-back,
.mod-inline-betting.narrow .bet-info-lay {
  margin-right: 3px;
  -ms-flex-negative: 0;
  flex-shrink: 0;
}
.mod-inline-betting.narrow .bet-actions-container {
  display: block;
  width: 100%;
}
.mod-inline-betting.narrow .inplay-bet-options-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  margin-bottom: 15px;
}
.mod-inline-betting.narrow .inplay-bet-options-container .at-inplay-label {
  font-weight: 700;
  margin-right: 12px;
}
.mod-inline-betting.narrow .inplay-bet-options-container form {
  -ms-flex-negative: 0;
  flex-shrink: 0;
}
.mod-inline-betting.narrow .inplay-bet-options-container label {
  margin-right: 12px;
}
.mod-inline-betting.narrow
  .inplay-bet-options-container
  label
  input[type="radio"] {
  margin: 1px 3px 0 0;
}
.mod-inline-betting.narrow .confirm-bet,
.mod-inline-betting.narrow .edit-bet,
.mod-inline-betting.narrow .place-bet,
.mod-inline-betting.narrow .price-container,
.mod-inline-betting.narrow .reset-bet,
.mod-inline-betting.narrow .size-container {
  width: calc(50% - 2px);
  max-width: none;
  margin: 0;
}
.mod-inline-betting.narrow .confirm-bet,
.mod-inline-betting.narrow .place-bet,
.mod-inline-betting.narrow .size-container {
  margin-left: 4px;
}
.mod-inline-betting.narrow .price-input,
.mod-inline-betting.narrow .size-input {
  margin: 0;
}
.mod-inline-betting.narrow .confirm-bet,
.mod-inline-betting.narrow .edit-bet,
.mod-inline-betting.narrow .place-bet,
.mod-inline-betting.narrow .reset-bet {
  margin-top: 4px;
  max-width: none;
}
.mod-inline-betting.narrow .separator {
  height: 20px;
  margin: 5px -3px 0 2px;
}
.mod-inline-betting.narrow .price-to-confirm,
.mod-inline-betting.narrow .size-to-confirm {
  -ms-flex-direction: row;
  flex-direction: row;
}
.mod-inline-betting.narrow .price-to-confirm .price-label,
.mod-inline-betting.narrow .price-to-confirm .size-label,
.mod-inline-betting.narrow .size-to-confirm .price-label,
.mod-inline-betting.narrow .size-to-confirm .size-label {
  margin-right: 4px;
}
.mod-inline-betting.narrow .nudges-visible .price-container .input,
.mod-inline-betting.narrow .nudges-visible .size-container .input {
  display: -ms-flexbox;
  display: flex;
}
.mod-inline-betting.narrow .nudges-visible .price-input,
.mod-inline-betting.narrow .nudges-visible .size-input {
  border-radius: 0;
}
.mod-inline-betting.narrow .nudges-visible .negative-nudge,
.mod-inline-betting.narrow .nudges-visible .positive-nudge {
  display: inline-block;
  min-width: 40px;
  width: 40px;
  height: 30px;
  padding: 10px 15px;
  outline: 0;
  border: 0;
  cursor: pointer;
  background-color: #bfbfbf;
}
.mod-inline-betting.narrow .nudges-visible .negative-nudge {
  border-radius: 2px 0 0 2px;
}
.mod-inline-betting.narrow .nudges-visible .positive-nudge {
  border-radius: 0 2px 2px 0;
}
.mod-inline-betting.narrow .nudges-visible .nudge-icon {
  width: 10px;
  height: 10px;
  fill: #1e1e1e;
}
.mod-inline-betting.narrow .nudges-visible .negative-nudge:disabled,
.mod-inline-betting.narrow .nudges-visible .positive-nudge:disabled {
  opacity: 0.5;
}
.mod-inline-betting.narrow .pnl-info-container {
  display: block;
  margin-bottom: 6px;
}
.mod-inline-betting.narrow .pnl-info-container .pnl-info {
  width: 100%;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
  margin-bottom: 4px;
}
.mod-inline-betting.narrow .pnl-info-container .pnl-info .outcome-label {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-right: 3px;
}
.mod-inline-betting.narrow .pnl-info-container .pnl-info .pnl-value.positive {
  color: #20a052;
}
.mod-inline-betting.narrow .pnl-info-container .pnl-info .pnl-value.negative {
  color: #d54d4d;
}
.mod-inline-betting.narrow .pnl-info-container .pnl-info:first-child {
  border-top: 1px solid #85adcc;
  padding-top: 10px;
}
.mod-inline-betting.narrow .pnl-info-container .pnl-info:last-child {
  margin-bottom: 0;
}
.mod-inline-betting.narrow .lay .pnl-info-container .pnl-info:first-child {
  border-top: 1px solid #e1b4bb;
}
.mod-inline-betting.narrow .loading-panel .message-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
}
.mod-inline-betting.narrow .notification-panel.error {
  -ms-flex-direction: column;
  flex-direction: column;
  -ms-flex-align: stretch;
  align-items: stretch;
}
.mod-inline-betting.narrow .notification-panel.error .message-container {
  margin: 0;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
.mod-inline-betting.narrow .notification-panel.error .button-container {
  display: -ms-flexbox;
  display: flex;
}
.mod-inline-betting.narrow .notification-panel.error .cancel-notification {
  margin: 8px 0 0;
  width: 100%;
}
.mod-inline-betting.narrow .notification-panel.error .edit-notification {
  margin: 8px 0 0 4px;
  width: 100%;
}
.mod-inline-betting.narrow .notification-panel.error .close-notification {
  margin: 0 8px 0 0;
}
.long-currency.mod-inline-betting.narrow .confirm-bet,
.long-currency.mod-inline-betting.narrow .place-bet,
.long-currency.mod-inline-betting.narrow .size-container {
  margin-left: 4px;
}
.long-currency.mod-inline-betting.narrow .separator {
  margin: 7px -6px 0 2px;
}
@media only screen and (orientation: portrait) {
  .long-currency.mod-inline-betting.narrow .confirm-bet,
  .long-currency.mod-inline-betting.narrow .edit-bet,
  .long-currency.mod-inline-betting.narrow .place-bet,
  .long-currency.mod-inline-betting.narrow .reset-bet {
    margin-top: 8px;
  }
  .long-currency.mod-inline-betting.narrow .confirm-bet,
  .long-currency.mod-inline-betting.narrow .edit-bet,
  .long-currency.mod-inline-betting.narrow .place-bet,
  .long-currency.mod-inline-betting.narrow .price-container,
  .long-currency.mod-inline-betting.narrow .reset-bet,
  .long-currency.mod-inline-betting.narrow .size-container {
    width: calc(50% - 2px);
  }
  .long-currency.mod-inline-betting.narrow .price-container,
  .long-currency.mod-inline-betting.narrow .size-container {
    width: 100%;
  }
  .long-currency.mod-inline-betting.narrow .size-container {
    margin-top: 8px;
    margin-left: 0;
  }
}
@media only screen and (orientation: landscape) {
  .long-currency.mod-inline-betting.narrow .confirm-bet,
  .long-currency.mod-inline-betting.narrow .edit-bet,
  .long-currency.mod-inline-betting.narrow .place-bet,
  .long-currency.mod-inline-betting.narrow .reset-bet {
    width: calc(50% - 2px);
    margin-top: 8px;
  }
  .long-currency.mod-inline-betting.narrow .edit-bet,
  .long-currency.mod-inline-betting.narrow .reset-bet {
    margin-left: 0;
  }
  .long-currency.mod-inline-betting.narrow .price-container,
  .long-currency.mod-inline-betting.narrow .size-container {
    width: calc(50% - 2px);
    -ms-flex: none;
    flex: none;
  }
}
.mod-inline-betting.line-betting-type .place-bet-panel,
.mod-inline-betting.line-betting-type .place-bet-panel.lay {
  background: #dcebea;
}
.mod-inline-betting.line-betting-type .separator {
  background-color: #519995;
}
.mod-inline-betting.line-betting-type .bet-info .extra-info {
  display: none;
}
.mod-inline-betting.line-betting-type.narrow
  .pnl-info-container
  .pnl-info:first-child {
  border-top: 1px solid #519995;
}
.mod-inline-betting.line-betting-type.narrow .bet-info .extra-info {
  display: block;
  margin-top: 2px;
}
.mod-quick-links {
  background-color: #fff;
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
  border-radius: 2px;
  color: #b8860b;
  font: 100% Arial, Regular;
  font-size: 12px;
  width: 100%;
}
.mod-quick-links .header {
  background-color: #303030;
  border-radius: 2px 2px 0 0;
  margin: 0;
  padding: 8px;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
}
.mod-quick-links .arrow {
  float: right;
  width: 9px;
  height: 14px;
  fill: #7f7f7f;
  transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  -webkit-transform: rotate(180deg);
}
.mod-quick-links .inplay-events-link {
  text-decoration: none;
  display: block;
  background-color: #20a052;
  color: #fff;
  font-weight: 700;
}
.mod-quick-links .inplay-events-link .inplay-counter {
  display: inline-block;
  padding: 8px;
  background-color: #4db375;
}
.mod-quick-links .inplay-events-link .inplay-label {
  display: inline-block;
  padding: 8px;
}
.mod-quick-links .inplay-events-link .arrow {
  padding: 8px;
  fill: #fff;
}
.mod-quick-links .links-list {
  list-style: none;
  margin: 0;
  padding: 0;
  border-radius: 2px;
}
.mod-quick-links .links-list .link {
  border-bottom: 1px solid #efefef;
  overflow: auto;
  width: 100%;
}
.mod-quick-links .links-list .link > a {
  overflow: auto;
}
.mod-quick-links .links-list .link .arrow,
.mod-quick-links .links-list .link .icon,
.mod-quick-links .links-list .link .label {
  display: inline-block;
  vertical-align: middle;
}
.mod-quick-links .links-list .link .icon {
  float: left;
  width: 12px;
  height: 14px;
}
.mod-quick-links .links-list .link .label {
  text-overflow: ellipsis;
  -webkit-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  float: left;
  color: #1e1e1e;
  line-height: 14px;
  max-width: calc(100% - 44px);
  margin: 0 8px;
}
.mod-quick-links .links-list .link a {
  text-decoration: none;
  display: block;
  padding: 8px;
}
.mod-quick-links .links-list .link:hover {
  background-color: #f6f6f6;
}
.mod-quick-links .collapse-button {
  padding: 8px;
  text-align: center;
  cursor: pointer;
}
.mod-quick-links .collapse-button .arrow {
  float: left;
  width: 9px;
  height: 14px;
  fill: #7f7f7f;
  transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  -webkit-transform: rotate(90deg);
  transition: transform 0.2s ease;
  -moz-transition: transform 0.2s ease;
  -webkit-transition: transform 0.2s ease;
}
.mod-quick-links .collapse-button.collapsed .arrow {
  transform: rotate(-90deg);
  -ms-transform: rotate(-90deg);
  -webkit-transform: rotate(-90deg);
}
.mod-quick-links .collapse-button .label {
  color: #1e1e1e;
  margin: 0 8px;
  font-weight: 700;
}
.mod-quick-links .clearfix:after {
  content: "";
  clear: both;
} /*! xsell-games-widget v1.0.4 (2019-11-28) */ /*! xsell-games-widget v1.0.4 (2019-11-28) */
.games-widget {
  font: 700 12px Arial, sans-serif;
  color: #1e1e1e;
  background-color: #fff;
}
.games-widget .widget-header {
  background-color: #1e1e1e;
  color: #fff;
  padding: 0 10px;
}
.games-widget .widget-content:after {
  content: "";
  display: block;
  clear: both;
}
.games-widget .widget-tabs {
  height: 30px;
  line-height: 30px;
  display: -ms-flexbox;
  display: flex;
}
.games-widget .widget-tab {
  background-color: #dfdfdf;
  -ms-flex: 1 1 25%;
  flex: 1 1 25%;
  padding: 0 5px;
  white-space: nowrap;
  text-align: center;
  border-left: 1px solid #fff;
}
.games-widget .widget-tab:first-child {
  border-left: 0;
}
.games-widget .widget-tab.selected {
  height: 30px;
  line-height: 30px;
  background-color: #fff;
}
.games-widget .widget-tabs.tabs-count-4 .widget-tab {
  -ms-flex: 1 1 25%;
  flex: 1 1 25%;
}
.games-widget .widget-tabs.tabs-count-4 .widget-tab.long-text,
.games-widget .widget-tabs.tabs-count-4 .widget-tab.long-text.selected {
  white-space: normal;
  line-height: normal;
}
.games-widget .widget-tabs.tabs-count-3 .widget-tab {
  -ms-flex: 1 1 33%;
  flex: 1 1 33%;
}
.games-widget .widget-tabs.tabs-count-2 .widget-tab {
  -ms-flex: 1 1 50%;
  flex: 1 1 50%;
}
.games-widget .widget-tabs.tabs-count-1 .widget-tab {
  -ms-flex: 1 1 100%;
  flex: 1 1 100%;
}
.games-widget .widget-tabs-content {
  overflow: hidden;
  position: relative;
}
.games-widget .widget-tab-content {
  display: none;
}
.games-widget .widget-tab-content:after {
  content: "";
  display: block;
  clear: both;
}
.games-widget .widget-tab-content.selected {
  display: block;
}
.games-widget .game-item {
  width: 50%;
  float: left;
  position: relative;
  padding: 0 0 2px 1px;
  box-sizing: border-box;
}
.games-widget .game-item .game-item-wrapper {
  display: block;
  overflow: hidden;
  padding-top: 65%;
  position: relative;
}
.games-widget .game-item .game-item-image {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  max-width: 100%;
  width: 100%;
  margin: auto;
}
.games-widget .game-item .game-item-overlay {
  width: 100%;
  vertical-align: top;
  display: none;
}
.games-widget .game-item:hover .game-item-overlay {
  display: block;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  position: absolute;
  height: 100%;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.5);
}
.games-widget .game-item .game-item-overlay-cta-wrapper {
  display: block;
  position: relative;
  text-align: center;
  margin-top: -8px;
  height: 16px;
}
.games-widget .game-item .game-item-default-cta {
  display: inline-block;
  height: 25px;
  border-radius: 2px;
  color: #303030;
  font-size: 10px;
  background-color: #dfdfdf;
  line-height: 25px;
  text-decoration: none;
  padding: 0 11px;
  vertical-align: top;
  min-width: 70%;
  max-width: 100%;
}
.games-widget .game-item .game-item-primary-cta {
  background-color: #ffb80c;
  color: #1e1e1e;
}
.games-widget .game-item .game-item-primary-cta:hover {
  background-color: #d99d0a;
}
.games-widget .game-item .game-item-primary-cta:active {
  background-color: #d99d0a;
  box-shadow: inset 0 2px 2px 0 rgba(0, 0, 0, 0.25);
}
.games-widget .widget-footer {
  text-align: right;
  clear: both;
}
.games-widget .widget-footer .widget-footer-label {
  cursor: pointer;
  color: #1e1e1e;
  text-decoration: none;
}
.games-widget .widget-footer .widget-footer-label .widget-footer-arrow {
  display: inline-block;
  position: relative;
  cursor: pointer;
  vertical-align: middle;
}
.games-widget.no-tabs.pp.horizontal {
  margin: 8px 8px 0;
  border-radius: 3px;
  box-shadow: 0 0 3px #bbb;
}
.games-widget.no-tabs.pp.horizontal .widget-content {
  padding: 0 4px 4px;
}
.games-widget.no-tabs.pp.horizontal .widget-content .game-item {
  width: 16.66%;
}
.games-widget.no-tabs.pp.horizontal .widget-content .game-item:nth-child(7n) {
  clear: both;
}
.games-widget.no-tabs.bf {
  box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.4);
}
.games-widget.no-tabs.bf .widget-header {
  background-color: #303030;
  line-height: 28px;
  border-radius: 2px 2px 0 0;
}
.games-widget.no-tabs.bf .game-item:nth-child(2n + 1) {
  clear: both;
  padding: 0 1px 2px 0;
}
.games-widget.no-tabs.bf .game-item .game-item-overlay-cta-wrapper {
  margin-top: -8px;
  top: 50%;
  height: 16px;
}
.games-widget.no-tabs.bf
  .game-item
  .two-bottons
  .game-item-overlay-cta-wrapper:nth-child(2n + 1) {
  top: 25%;
}
.games-widget.no-tabs.bf
  .game-item
  .two-bottons
  .game-item-overlay-cta-wrapper:nth-child(2n) {
  top: 55%;
}
.games-widget.no-tabs.bf .widget-footer {
  height: 28px;
  border-radius: 0 0 4px 4px;
}
.games-widget.no-tabs.bf .widget-footer .widget-footer-label {
  line-height: 28px;
  cursor: pointer;
}
.games-widget.no-tabs.bf .widget-footer .widget-footer-label:hover {
  text-decoration: underline;
}
.games-widget.no-tabs.bf
  .widget-footer
  .widget-footer-label
  .widget-footer-arrow {
  width: 9px;
  height: 6px;
  line-height: 28px;
  transition: transform 0.3s ease;
  transform: rotate(180deg);
  margin: 0 8px 0 4px;
}
.games-widget.no-tabs.bf
  .widget-footer
  .widget-footer-label
  .widget-footer-arrow.list-expanded {
  transform: rotate(0deg);
}
.games-widget.no-tabs.pp * {
  box-sizing: border-box;
}
.games-widget.no-tabs.pp .widget-header {
  font-size: 16px;
  background: 0 0;
  color: #444;
  font-weight: 400;
  padding: 14px 8px 10px;
}
.games-widget.no-tabs.pp .widget-content {
  padding: 0 4px;
}
.games-widget.no-tabs.pp .widget-content .game-item {
  padding: 4px;
}
.games-widget.no-tabs.pp
  .widget-content
  .game-item
  .game-item-overlay-cta-wrapper {
  position: absolute;
  margin-top: 100%;
  height: 36px;
  bottom: 4px;
  width: 100%;
  padding: 0 4px;
}
.games-widget.no-tabs.pp .widget-content .game-item .game-item-primary-cta {
  height: 36px;
  line-height: 36px;
  width: 100%;
  border-radius: 2px;
  background-color: #9f2741;
  box-shadow: inset 0 -2px 0 0 rgba(0, 0, 0, 0.2);
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -0.1px;
  color: #fff;
}
.games-widget.no-tabs.pp
  .widget-content
  .game-item
  .two-bottons
  .game-item-overlay-cta-wrapper:nth-child(2n + 1) {
  display: none;
}
.games-widget.no-tabs.pp .widget-footer {
  padding-top: 4px;
}
.games-widget.no-tabs.pp .widget-footer .widget-footer-label {
  display: none;
}
.games-widget.no-tabs.pp.vertical .widget-content .game-item:nth-child(2n + 1) {
  clear: both;
}
.mod-todays-racing .country-tab,
.mod-todays-racing .more-flag {
  display: inline-block;
  vertical-align: middle;
}
.mod-todays-racing .header::after,
.mod-todays-racing .race-list::after {
  clear: both;
}
.mod-todays-racing {
  font: 100% Arial, Regular;
  color: #1e1e1e;
  font-size: 11px;
  font-weight: 700;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.4);
}
.mod-todays-racing .todays-racing-loading-countries,
.mod-todays-racing .todays-racing-loading-meetings {
  text-align: center;
  padding-top: 37px;
  padding-bottom: 37px;
  background-color: #fff;
}
.mod-todays-racing .header {
  background-color: #303030;
  padding: 8px;
  border-radius: 2px 2px 0 0;
}
.mod-todays-racing .header-title {
  font-size: 12px;
  line-height: 12px;
  color: #fff;
}
.mod-todays-racing .header-schedule-filters {
  float: right;
}
.mod-todays-racing .country-tabs-container {
  list-style-type: none;
  padding: 0;
  margin: 0;
  width: 100%;
  background-color: #efefef;
  border-bottom: 1px solid #dfdfdf;
  height: 45px;
}
.mod-todays-racing .country-tab {
  background-color: #efefef;
  text-align: center;
  border-right: 1px solid #dfdfdf;
  cursor: pointer;
  width: 85px;
}
.mod-todays-racing .country-tab:focus,
.mod-todays-racing .country-tab:hover {
  background-color: #e4e4e4;
}
.mod-todays-racing .country-tab.more {
  position: relative;
  line-height: 12px;
}
.mod-todays-racing .country-tab.active,
.mod-todays-racing .country-tab.more.active {
  border-top: 2px solid #ffb80c;
  background-color: #fff;
}
.mod-todays-racing .more-country-tab {
  padding: 8px;
}
.mod-todays-racing .more-country-tab:focus,
.mod-todays-racing .more-country-tab:hover {
  background-color: #e4e4e4;
}
.mod-todays-racing .tab-wrapper {
  height: 44px;
}
.mod-todays-racing .grouped-countries-tab-wrapper .flag {
  padding: 0 5px;
}
.mod-todays-racing .flag,
.mod-todays-racing .more-flag {
  width: 20px;
  height: 12px;
}
.mod-todays-racing .flag {
  margin: 8px auto 4px;
}
.mod-todays-racing .country-label {
  vertical-align: middle;
}
.mod-todays-racing .more-dropdown {
  list-style-type: none;
  padding: 0;
  margin: 0;
  width: 100%;
  position: absolute;
  top: 44px;
  background-color: #fff;
  text-align: left;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.3);
}
.mod-todays-racing .more-label {
  height: 100%;
  line-height: 44px;
  vertical-align: middle;
  padding-right: 4px;
}
.mod-todays-racing .more-icon {
  width: 9px;
  height: 5px;
  vertical-align: baseline;
  fill: #999;
}
.mod-todays-racing .country-content .live-video-icon,
.mod-todays-racing .country-content .meeting-description,
.mod-todays-racing .country-content .meeting-info,
.mod-todays-racing .country-content .race-list,
.mod-todays-racing .more-active-country {
  display: inline-block;
  vertical-align: middle;
}
.mod-todays-racing .country-content {
  width: 100%;
  background-color: #fff;
  list-style-type: none;
  border-radius: 0 0 2px 2px;
}
.mod-todays-racing .country-content .meeting-item {
  border-bottom: 1px solid #efefef;
  padding: 8px 0 8px 8px;
}
.mod-todays-racing .country-content .meeting-item:last-child {
  border: 0;
}
.mod-todays-racing .country-content .meeting-item::before {
  content: "";
  display: inline-block;
  vertical-align: middle;
  min-height: 32px;
}
.mod-todays-racing .country-content .meeting-info {
  width: 250px;
}
.mod-todays-racing .country-content .meeting-description {
  padding-right: 8px;
  width: 80%;
}
.mod-todays-racing .country-content .meeting-label,
.mod-todays-racing .country-content .racetrack-conditions {
  font-size: 12px;
}
.mod-todays-racing .country-content .racetrack-conditions {
  font-weight: 400;
}
.mod-todays-racing .country-content .live-video-icon {
  padding: 8px 8px 0 0;
  fill: #7f7f7f;
  margin: 4px 0;
}
.mod-todays-racing .country-content .live-video-icon .icon {
  width: 16px;
  height: 16px;
}
.mod-todays-racing .empty-content {
  text-align: center;
  padding-top: 37px;
  padding-bottom: 37px;
  background-color: #fff;
}
.mod-todays-racing .empty-content .no-content-message {
  font-weight: 700;
}
.mod-todays-racing .race-list {
  margin: 0;
  padding: 0;
  width: calc(100% - 250px);
}
.mod-todays-racing .race-list .race-information {
  float: left;
  list-style-type: none;
  margin: 2px 4px 2px 0;
}
.mod-todays-racing .race-list .race-link {
  display: block;
  background-color: #dfdfdf;
  padding: 0 16px;
  border-radius: 2px;
  text-decoration: none;
  color: #1e1e1e;
  height: 28px;
}
.mod-todays-racing .race-list .race-link:focus,
.mod-todays-racing .race-list .race-link:hover {
  background-color: #c2c2c2;
}
.mod-todays-racing .race-list .race-link.inplay-state {
  padding: 0 10px 0 8px;
}
.mod-todays-racing .race-list .race-link.results-state {
  background-color: #c2c2c2;
  padding: 0 7px 0 8px;
}
.mod-todays-racing .race-list .race-link.results-state:focus,
.mod-todays-racing .race-list .race-link.results-state:hover {
  background-color: #a0a0a0;
}
.mod-todays-racing .race-list .race-link .label {
  display: inline-block;
  vertical-align: top;
  line-height: 28px;
}
.mod-todays-racing .race-list .inplay-icon {
  display: inline-block;
  margin-top: 9px;
}
.mod-todays-racing .race-list .inplay-icon .icon {
  width: 14px;
  height: 10px;
}
.mod-todays-racing .race-list .results-icon {
  margin-top: 6px;
  display: inline-block;
}
.mod-todays-racing .race-list .results-icon .icon {
  width: 14px;
  height: 16px;
}
.bf-tooltip {
  visibility: hidden;
  display: table;
  position: absolute;
  right: -10px;
  bottom: 18px;
  background: #fff;
  box-shadow: 0 0 8px 0 #3b5160;
  width: 200px;
  padding: 12px 8px;
  white-space: pre-wrap;
  z-index: 10;
}
.bf-tooltip:after {
  content: "";
  width: 10px;
  height: 10px;
  display: block;
  background: #fff;
  border: 1px solid #3b5160;
  border-color: transparent #bbb #bbb transparent;
  transform: rotate(45deg);
  position: absolute;
  bottom: -6px;
  right: 10px;
  z-index: 0;
}
.bf-tooltip .text {
  color: #3b5160;
  line-height: 1.2em;
  display: table-cell;
}
.bf-tooltip.has-close-button .close-button {
  display: table-cell;
  cursor: pointer;
  width: 20px;
}
.bf-tooltip.has-close-button .close-button:after,
.bf-tooltip.has-close-button .close-button:before {
  position: absolute;
  width: 2px;
  height: 16px;
  background-color: #444;
  content: " ";
  right: 6px;
}
.bf-tooltip.has-close-button .close-button:before {
  transform: rotate(45deg);
}
.bf-tooltip.has-close-button .close-button:after {
  transform: rotate(-45deg);
}
.bf-tooltip.visible {
  visibility: visible;
}
.bf-tooltip * {
  z-index: 1;
  position: relative;
}
.bf-tooltip-wrapper {
  visibility: hidden;
  display: inline;
}
.bf-tooltip-wrapper.bottom .bf-tooltip {
  bottom: auto;
  top: 18px;
}
.bf-tooltip-wrapper.bottom .bf-tooltip:after {
  bottom: auto;
  top: -6px;
  transform: rotate(225deg);
}
.bf-tooltip-wrapper.center {
  position: absolute;
  left: 50%;
  display: inline-block;
}
.bf-tooltip-wrapper.center .bf-tooltip {
  position: relative;
  left: -50%;
  width: auto;
  margin-left: 2px;
  max-width: 200px;
  bottom: auto;
}
.bf-tooltip-wrapper.center .bf-tooltip:after {
  right: 50%;
  transform: translate(5px) rotate(225deg);
}
.bf-tooltip-wrapper.center.top {
  bottom: 100%;
}
.bf-tooltip-wrapper.center.top .bf-tooltip:after {
  transform: translate(5px) rotate(45deg);
}
.bf-tooltip-wrapper.middle.left,
.bf-tooltip-wrapper.middle.right {
  position: absolute;
  left: 0;
  top: 50%;
}
.bf-tooltip-wrapper.middle.left .bf-tooltip,
.bf-tooltip-wrapper.middle.right .bf-tooltip {
  left: 22px;
  position: relative;
}
.bf-tooltip-wrapper.middle.left .bf-tooltip:after,
.bf-tooltip-wrapper.middle.right .bf-tooltip:after {
  top: 0;
  transform: translate(-16px, 9px) rotate(135deg);
}
.bf-tooltip-wrapper.middle.left.left,
.bf-tooltip-wrapper.middle.right.left {
  left: auto;
  right: 0;
}
.bf-tooltip-wrapper.middle.left.left .bf-tooltip,
.bf-tooltip-wrapper.middle.right.left .bf-tooltip {
  left: auto;
  right: 22px;
}
.bf-tooltip-wrapper.middle.left.left .bf-tooltip:after,
.bf-tooltip-wrapper.middle.right.left .bf-tooltip:after {
  transform: translate(16px, 9px) rotate(-45deg);
}
.bf-tooltip-wrapper.right .bf-tooltip {
  left: -10px;
  right: auto;
}
.bf-tooltip-wrapper.right .bf-tooltip:after {
  right: auto;
  left: 10px;
}
.bf-tooltip-wrapper.rounded .bf-tooltip {
  border-radius: 3px;
}
.bf-tooltip-parent {
  position: relative;
}
.bf-tooltip-parent:hover .bf-tooltip:not(.has-close-button) {
  visibility: visible;
}
#tooltip-step-overlay * {
  position: fixed;
  z-index: 999999;
  background-color: #1e1e1e;
  opacity: 0.8;
}
.tooltip-step-modal {
  z-index: 1000000;
  position: absolute;
  visibility: hidden;
  background-color: #fff;
  width: 418px;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  box-shadow: 0 1px 10px rgba(0, 0, 0, 0.4);
  transition: all 0.3s ease-out;
}
.tooltip-step-modal .tooltip-step-header-container {
  background-color: #fff;
  padding: 15px 12px;
  border-bottom: 1px solid #dfdfdf;
  position: relative;
}
.tooltip-step-modal .tooltip-step-header-container .tooltip-step-header {
  font-size: 14px;
  color: #1e1e1e;
  font-weight: 700;
}
.tooltip-step-modal .tooltip-step-header-container .tooltip-step-close-button {
  position: absolute;
  top: 17px;
  right: 12px;
  width: 12px;
  height: 12px;
  cursor: pointer;
}
.tooltip-step-modal
  .tooltip-step-header-container
  .tooltip-step-close-button
  .close-button-icon {
  width: 12px;
  height: 12px;
}
.tooltip-step-modal .tooltip-step-subtitle {
  line-height: 14px;
  font-size: 12px;
  font-weight: 700;
  text-align: left;
  color: #303030;
  margin: 15px 12px;
}
.tooltip-step-modal .tooltip-step-body {
  background-color: #fff;
  font-size: 11px;
  line-height: 18px;
  color: #1e1e1e;
  font-weight: 400;
  margin: 15px 12px;
  text-align: left;
}
.tooltip-step-modal .tooltip-arrow {
  border: 5px solid #fff;
  content: "";
  position: absolute;
}
.tooltip-step-modal .tooltip-arrow.top,
.tooltip-step-modal .tooltip-arrow.top-middle,
.tooltip-step-modal .tooltip-arrow.top-right {
  top: -10px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: #fff;
  border-left-color: transparent;
}
.tooltip-step-modal .tooltip-arrow.top-right {
  right: 10px;
}
.tooltip-step-modal .tooltip-arrow.top-middle {
  left: 50%;
  margin-left: -5px;
}
.tooltip-step-modal .tooltip-arrow.right,
.tooltip-step-modal .tooltip-arrow.right-bottom {
  right: -10px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  border-left-color: #fff;
}
.tooltip-step-modal .tooltip-arrow.right {
  top: 10px;
}
.tooltip-step-modal .tooltip-arrow.right-bottom {
  bottom: 10px;
}
.tooltip-step-modal .tooltip-arrow.bottom {
  bottom: -10px;
  border-top-color: #fff;
  border-right-color: transparent;
  border-bottom-color: transparent;
  border-left-color: transparent;
}
.tooltip-step-modal .tooltip-arrow.left,
.tooltip-step-modal .tooltip-arrow.left-bottom {
  left: -10px;
  border-top-color: transparent;
  border-right-color: #fff;
  border-bottom-color: transparent;
  border-left-color: transparent;
}
.tooltip-step-modal .tooltip-arrow.left {
  top: 10px;
}
.tooltip-step-modal .tooltip-arrow.left-bottom {
  bottom: 10px;
}
.tooltip-step-modal .tooltip-are-you-sure-step-button-container {
  text-align: center;
  background-color: #f6f6f6;
  border-top: 1px solid #dfdfdf;
}
.tooltip-step-modal .tooltip-done-step-button-container {
  position: absolute;
  z-index: 1;
  right: 0;
  clear: both;
}
.tooltip-step-modal .tooltip-button {
  font-weight: 700;
  text-align: center;
  width: 64px;
  height: 24px;
  line-height: 24px;
  border: 0;
  padding: 0;
  margin: 7px 12px;
}
.tooltip-step-modal .tooltip-button.are-you-sure-step-cancel-button {
  background-color: #dfdfdf;
  color: #1e1e1e;
  float: left;
}
.tooltip-step-modal .tooltip-button.are-you-sure-step-continue-button,
.tooltip-step-modal .tooltip-button.done-step-button {
  background-color: #ffb80c;
  color: #1e1e1e;
  float: right;
}
.tooltip-step-modal .tooltip-button.left-button {
  background-color: #bfbfbf;
}
.tooltip-step-bullets {
  position: relative;
  height: 40px;
  text-align: center;
  background-color: #f6f6f6;
  border-top: 1px solid #dfdfdf;
}
.tooltip-step-bullets .tooltip-navigation-buttons-container {
  position: absolute;
  left: 0;
  width: 100%;
  z-index: 0;
}
.tooltip-step-bullets .tooltip-next-step,
.tooltip-step-bullets .tooltip-prev-step {
  width: 6px;
  height: 9px;
  display: inline-block;
  cursor: pointer;
}
.tooltip-step-bullets .tooltip-next-step .left-arrow-icon,
.tooltip-step-bullets .tooltip-next-step .right-arrow-icon,
.tooltip-step-bullets .tooltip-prev-step .left-arrow-icon,
.tooltip-step-bullets .tooltip-prev-step .right-arrow-icon {
  width: 6px;
  height: 9px;
  margin: 15px 12px;
}
.tooltip-step-bullets .tooltip-next-step .left-arrow-icon,
.tooltip-step-bullets .tooltip-prev-step .left-arrow-icon {
  margin: 5px 12px;
}
.tooltip-step-bullets .tooltip-prev-step {
  transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  -webkit-transform: rotate(180deg);
}
.tooltip-step-bullets .left-container {
  position: absolute;
  left: 0;
  z-index: 1;
}
.tooltip-step-bullets .tooltip-step-bullets-list {
  clear: both;
  margin: 15px 0;
  padding: 0;
  display: inline-block;
}
.tooltip-step-bullets
  .tooltip-step-bullets-list
  .tooltip-step-bullets-list-item {
  list-style: none;
  float: left;
  margin: 0 2px;
}
.tooltip-step-bullets
  .tooltip-step-bullets-list
  .tooltip-step-bullets-list-item
  .tooltip-step-bullets-anchor {
  display: block;
  width: 8px;
  height: 8px;
  border-radius: 10px;
  -moz-border-radius: 10px;
  -webkit-border-radius: 10px;
  text-decoration: none;
  background-color: #dfdfdf;
}
.tooltip-step-bullets
  .tooltip-step-bullets-list
  .tooltip-step-bullets-list-item.bullet-default
  .tooltip-step-bullets-anchor.tooltip-step-bullets-active,
.tooltip-step-bullets
  .tooltip-step-bullets-list
  .tooltip-step-bullets-list-item.bullet-default
  .tooltip-step-bullets-anchor.tooltip-step-bullets-active:hover {
  background-color: #ffb80c;
}
.tooltip-step-bullets
  .tooltip-step-bullets-list
  .tooltip-step-bullets-list-item.bullet-alternative1
  .tooltip-step-bullets-anchor.tooltip-step-bullets-active,
.tooltip-step-bullets
  .tooltip-step-bullets-list
  .tooltip-step-bullets-list-item.bullet-alternative1
  .tooltip-step-bullets-anchor.tooltip-step-bullets-active:hover {
  background-color: #a6d8ff;
}
.tooltip-step-bullets
  .tooltip-step-bullets-list
  .tooltip-step-bullets-list-item.bullet-alternative2
  .tooltip-step-bullets-anchor.tooltip-step-bullets-active,
.tooltip-step-bullets
  .tooltip-step-bullets-list
  .tooltip-step-bullets-list-item.bullet-alternative2
  .tooltip-step-bullets-anchor.tooltip-step-bullets-active:hover {
  background-color: #fac9d4;
}
.mod-cashout {
  font-size: 11px;
  background-color: #fff;
  color: #303030;
}
.mod-cashout .cashout-liability-value {
  font-weight: 700;
}
.mod-cashout .cashout-liability-label,
.mod-cashout .cashout-liability-value {
  font-size: 11px;
  line-height: 12px;
  vertical-align: middle;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
.mod-cashout .cashout-button {
  font-size: 12px;
  text-align: center;
  box-sizing: border-box;
  padding: 3px;
  display: inline-block;
  vertical-align: middle;
  height: 38px;
  background: #ffb80c;
  border-width: 0;
  border-radius: 2px;
  margin: 0 8px;
  cursor: pointer;
  min-width: 142px;
  max-width: 248px;
}
.mod-cashout .cashout-button:hover {
  background: #e6a40b;
}
.mod-cashout .cashout-button.disabled {
  cursor: auto;
  background: #ffdc86;
  color: rgba(30, 30, 30, 0.5);
}
.mod-cashout .cashout-button:not(.disabled) .cashout-button-profit-value {
  color: #20a052;
}
.mod-cashout
  .cashout-button:not(.disabled)
  .cashout-button-profit-value.negative {
  color: #d54d4d;
}
.mod-cashout .cashout-button-amount,
.mod-cashout .cashout-button-profit {
  line-height: 16px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: center;
  justify-content: center;
  margin: auto 5px;
}
.mod-cashout .cashout-button-amount-label,
.mod-cashout .cashout-button-amount-value,
.mod-cashout .cashout-button-profit-label,
.mod-cashout .cashout-button-profit-value {
  overflow: hidden;
  text-overflow: ellipsis;
  display: inline-block;
  vertical-align: top;
  white-space: nowrap;
}
.mod-cashout .cashout-button-amount-label,
.mod-cashout .cashout-button-profit-label {
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  text-align: right;
  margin-right: 2px;
}
.mod-cashout .cashout-button-amount-value,
.mod-cashout .cashout-button-profit-value {
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  text-align: left;
  margin-left: 2px;
}
.mod-cashout .cashout-button-amount,
.mod-cashout .cashout-button-profit-value {
  font-weight: 700;
}
.mod-cashout .action-button {
  display: inline-block;
  height: 38px;
  box-sizing: border-box;
  padding: 13px 4px;
  border: 0;
  border-radius: 2px;
  outline: 0;
  cursor: pointer;
  background-color: #dcdcdc;
  font-size: 11px;
  text-align: center;
  color: #303030;
  font-weight: 700;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.mod-cashout .action-button:hover {
  background-color: #c2c2c2;
}
.mod-cashout .tabbed-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  -ms-flex-pack: center;
  justify-content: center;
  -ms-flex-align: center;
  align-items: center;
  padding-top: 8px;
  height: 28px;
}
.mod-cashout .auto-cashout-container {
  font-size: 12px;
}
.mod-cashout .auto-cashout-button-container,
.mod-cashout .auto-cashout-label-input-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
}
.mod-cashout .auto-cashout-input {
  padding: 0 4px;
  outline: 0;
  height: 28px;
  margin: 0 8px;
  max-width: 98px;
  border-radius: 2px;
  border: 1px solid #424242;
  text-align: center;
}
.mod-cashout .auto-cashout-label-input-container .help-link-container {
  display: none;
}
.mod-cashout .auto-cashout-button {
  height: 28px;
  margin: 0 8px;
  padding: 0 4px;
}
.mod-cashout .auto-cashout-button:disabled {
  background-color: #dcdcdc;
  cursor: default;
}
.mod-cashout .auto-cashout-save {
  color: #303030;
}
.mod-cashout .auto-cashout-save:disabled {
  color: #7f7f7f;
}
.mod-cashout .auto-cashout-remove {
  color: #d54d4d;
}
.mod-cashout .auto-cashout-button-label {
  padding: 8px;
}
.mod-cashout .auto-cashout-message-container,
.mod-cashout .auto-cashout-saved-label-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: center;
  justify-content: center;
  -ms-flex-line-pack: center;
  align-content: center;
  overflow: hidden;
}
.mod-cashout .auto-cashout-saved-label-container {
  padding-right: 4px;
}
.mod-cashout .auto-cashout-saved-value {
  font-weight: 700;
  padding-left: 4px;
}
.mod-cashout .auto-cashout-message-container {
  padding-left: 4px;
}
.mod-cashout .auto-cashout-message-label,
.mod-cashout .auto-cashout-saved-label {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
.mod-cashout .auto-cashout-message-label {
  color: #20a052;
  font-weight: 700;
}
.mod-cashout .auto-cashout-removed-message {
  color: #d54d4d;
}
.mod-cashout .auto-cashout-icon {
  width: 12px;
  height: 12px;
  margin: 0 4px;
}
.mod-cashout .auto-cashout-saved-dot {
  position: absolute;
  background-color: #20a052;
  height: 8px;
  width: 8px;
  top: -2px;
  right: -2px;
  border-radius: 4px;
}
.mod-cashout.narrow .auto-cashout-button-container,
.mod-cashout.narrow .auto-cashout-label-input-container {
  overflow: hidden;
}
.mod-cashout.mini .auto-cashout-container,
.mod-cashout.small .auto-cashout-container {
  -ms-flex-flow: column;
  flex-flow: column;
  -ms-flex-pack: distribute;
  justify-content: space-around;
  height: 70px;
}
.mod-cashout.mini .auto-cashout-button-container .help-link-container,
.mod-cashout.small .auto-cashout-button-container .help-link-container {
  display: none;
}
.mod-cashout.mini .auto-cashout-button-container,
.mod-cashout.mini .auto-cashout-label-input-container,
.mod-cashout.small .auto-cashout-button-container,
.mod-cashout.small .auto-cashout-label-input-container {
  width: 100%;
}
.mod-cashout.mini .auto-cashout-button-container,
.mod-cashout.small .auto-cashout-button-container {
  margin-top: 8px;
}
.mod-cashout.mini .auto-cashout-remove-button-container,
.mod-cashout.small .auto-cashout-remove-button-container {
  margin-top: 0;
}
.mod-cashout.mini .auto-cashout-button,
.mod-cashout.small .auto-cashout-button {
  width: 100%;
  max-width: 300px;
}
.mod-cashout.mini .auto-cashout-message-container,
.mod-cashout.mini .auto-cashout-saved-label-container,
.mod-cashout.small .auto-cashout-message-container,
.mod-cashout.small .auto-cashout-saved-label-container {
  max-width: 100%;
  padding: 0;
}
.mod-cashout.small .auto-cashout-label-input-container .help-link-container {
  display: inline-block;
}
.mod-cashout.mini .auto-cashout-input {
  margin-right: 0;
  max-width: 68px;
}
.mod-cashout button,
.mod-cashout input {
  font-family: inherit;
}
.mod-cashout .cashout-button-panel {
  padding: 8px;
}
.mod-cashout .cashout-button-panel.no-expandable-content .help-link-container {
  margin-left: 0;
}
.mod-cashout
  .cashout-button-panel.no-expandable-content
  .help-link-container.no-expandable-content {
  display: inline-block;
}
.mod-cashout .cashout-button-panel .cashout-button-panel-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
}
.mod-cashout .cashout-button-panel .cashout-liability {
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
}
.mod-cashout .cashout-button-panel .cashout-button {
  -ms-flex: 1;
  flex: 1;
}
.mod-cashout .cashout-button-panel .slider-container {
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  display: inline-block;
  vertical-align: middle;
}
.mod-cashout .cashout-button-panel .slider {
  -ms-flex: 1 0 auto;
  flex: 1 0 auto;
  width: 204px;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -ms-flex-align: center;
  align-items: center;
  margin: 0 12px;
  height: 12px;
  vertical-align: middle;
}
.mod-cashout .cashout-button-panel .slider-label {
  color: #7f7f7f;
  display: inline-block;
  font-size: 11px;
  line-height: 12px;
  vertical-align: middle;
}
.mod-cashout .cashout-button-panel .help-link,
.mod-cashout .cashout-button-panel .help-link-container {
  width: 16px;
  height: 16px;
}
.mod-cashout .cashout-button-panel .help-link-container {
  margin-left: 8px;
  cursor: help;
  -ms-flex-negative: 0;
  flex-shrink: 0;
}
.mod-cashout .cashout-button-panel .help-link-container.no-expandable-content {
  display: none;
}
.mod-cashout .cashout-button-panel .help-link-icon {
  width: 100%;
  height: 100%;
}
.mod-cashout .cashout-button-panel .expandable-content {
  margin: 8px auto 0;
}
.mod-cashout .cashout-button-panel .expand-button {
  -ms-flex-negative: 0;
  flex-shrink: 0;
  width: 38px;
  height: 38px;
  padding: 0;
  position: relative;
  overflow: visible;
}
.mod-cashout .cashout-button-panel .expand-icon {
  fill: #303030;
  width: 18px;
  height: 18px;
  object-fit: contain;
}
.mod-cashout .cashout-button-panel .expand-icon.auto-cashout-set {
  fill: #20a052;
}
.mod-cashout .cashout-tabs-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  -ms-flex-pack: center;
  justify-content: center;
}
.mod-cashout .tab {
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  width: 140px;
  font-size: 12px;
  padding: 10px 4px;
  color: #303030;
  text-align: center;
  cursor: pointer;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.mod-cashout .tab.selected {
  border-bottom: 2px solid #303030;
  font-weight: 700;
}
.mod-cashout .tab:not(.selected):hover {
  border-bottom: 2px solid #c2c2c2;
}
.mod-cashout .cashout-button-panel:not(.collapsed) .expand-button {
  background-color: #c2c2c2;
}
.mod-cashout .cashout-button-panel.collapsed .expandable-content,
.mod-cashout.mini .cashout-button-panel .cashout-liability,
.mod-cashout.mini .cashout-button-panel .help-link-container {
  display: none;
}
.mod-cashout.mini .cashout-button-panel .cashout-button {
  margin-left: 0;
}
.mod-cashout.mini .cashout-button-panel .slider-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex: 1 0 auto;
  flex: 1 0 auto;
}
.mod-cashout.mini .cashout-button-panel .slider {
  width: 136px;
}
.mod-cashout .confirmation-panel {
  padding: 8px;
}
.mod-cashout .confirmation-panel .confirmation-panel-container {
  display: block;
}
.mod-cashout .confirmation-panel .confirmation-panel-controls {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
}
.mod-cashout
  .confirmation-panel
  .confirmation-panel-controls
  .cashout-confirmation-cancel-button {
  -ms-flex: 0 0 91px;
  flex: 0 0 91px;
  height: 38px;
}
.mod-cashout .confirmation-panel .confirmation-panel-controls .cashout-button {
  -ms-flex: 1;
  flex: 1;
}
.mod-cashout .confirmation-panel .cashout-confirmation-message-container {
  display: inline-block;
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  text-align: left;
}
.mod-cashout
  .confirmation-panel
  .cashout-confirmation-message-container.compact-view {
  display: none;
  margin-top: 6px;
}
.mod-cashout .confirmation-panel .cashout-confirmation-option-checkbox {
  margin: 0 4px 0 0;
  vertical-align: middle;
}
.mod-cashout.narrow
  .confirmation-panel
  .cashout-confirmation-message-container {
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  max-width: 200px;
}
.mod-cashout.small .confirmation-panel .cashout-confirmation-message-container {
  margin-left: auto;
  margin-right: auto;
  max-width: 348px;
}
.mod-cashout.mini .confirmation-panel .cashout-button,
.mod-cashout.small .confirmation-panel .cashout-button {
  margin-right: 0;
  width: 134px;
  min-width: 134px;
}
.mod-cashout.mini .confirmation-panel .cashout-confirmation-message-container,
.mod-cashout.small .confirmation-panel .cashout-confirmation-message-container {
  display: none;
}
.mod-cashout.mini
  .confirmation-panel
  .cashout-confirmation-message-container.compact-view,
.mod-cashout.small
  .confirmation-panel
  .cashout-confirmation-message-container.compact-view {
  display: block;
  text-align: center;
}
.mod-cashout.mini .confirmation-panel .cashout-confirmation-option,
.mod-cashout.small .confirmation-panel .cashout-confirmation-option {
  margin-top: 2px;
}
.mod-cashout.mini .confirmation-panel .cashout-confirmation-cancel-button {
  -ms-flex: 0 0 66px;
  flex: 0 0 66px;
}
.mod-cashout .progress-container {
  background: #efefef;
  position: relative;
  height: 50px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  z-index: 2;
}
.mod-cashout .progress-message-container {
  padding-left: 8px;
}
.mod-cashout .progress-message-container .message {
  font-weight: 700;
}
.mod-cashout .progress-message-container .message-title {
  font-weight: 400;
}
.mod-cashout .progress-message-container .message-content {
  font-weight: 700;
}
.mod-cashout .progress-bar-container {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  z-index: -1;
  background: #fff;
}
.mod-cashout .progress-bar {
  background-color: #dfdfdf;
  height: 50px;
}
.mod-cashout .cashout-notification-container {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  width: 100%;
  height: 50px;
  border: solid 1px #dedede;
  white-space: nowrap;
  background-color: #dfdfdf;
}
.mod-cashout .cashout-notification-container.generic-notification {
  background-color: #dfdfdf;
  color: #1e1e1e;
}
.mod-cashout
  .cashout-notification-container.generic-notification
  .notification-close-icon {
  fill: #1e1e1e;
}
.mod-cashout .cashout-notification-container.successful-notification {
  background-color: #20a052;
  color: #fff;
}
.mod-cashout .cashout-notification-container.unsuccessful-notification {
  background-color: #d54d4d;
  color: #fff;
}
.mod-cashout .cashout-notification-container.warning-notification {
  background-color: #fff8d6;
  color: #8a6d3b;
}
.mod-cashout
  .cashout-notification-container.warning-notification
  .notification-close-icon {
  fill: #8a6d3b;
}
.mod-cashout .cashout-notification-container .notification-content-container {
  margin-left: 8px;
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  min-width: 0;
  margin-right: 8px;
}
.mod-cashout .cashout-notification-container .cashout-notification-text {
  text-overflow: ellipsis;
  overflow: hidden;
  display: block;
}
.mod-cashout .cashout-notification-container .cashout-notification-message {
  font-weight: 700;
}
.mod-cashout .cashout-notification-container .notification-close-container {
  width: 24px;
  height: 100%;
  margin-left: auto;
  -ms-flex: 0 0 auto;
  flex: 0 0 auto;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
  cursor: pointer;
}
.mod-cashout .cashout-notification-container .notification-close-icon {
  width: 8px;
  height: 8px;
  fill: #fff;
  fill-opacity: 0.5;
}
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .mod-cashout .cashout-button-panel {
    text-align: center;
  }
  .mod-cashout .cashout-button-panel .cashout-button-panel-container {
    display: block;
  }
  .mod-cashout .cashout-button-panel .cashout-liability {
    text-align: left;
  }
  .mod-cashout .cashout-button-panel .tabbed-container {
    width: 100%;
  }
  .mod-cashout .cashout-button-panel .cashout-button,
  .mod-cashout .cashout-button-panel .cashout-liability,
  .mod-cashout .cashout-button-panel .expand-button,
  .mod-cashout .cashout-button-panel .help-link-container,
  .mod-cashout .cashout-button-panel .slider-container {
    display: inline-block;
    vertical-align: middle;
  }
  .mod-cashout .cashout-button-panel .cashout-button {
    width: 240px;
  }
  .mod-cashout
    .cashout-button-panel
    .auto-cashout-label-input-container
    .help-link-container {
    display: none;
  }
  .mod-cashout .cashout-button-panel:not(.collapsed) .expandable-content {
    display: block;
  }
  .mod-cashout.mini .cashout-button-panel .expandable-content,
  .mod-cashout.narrow .cashout-button-panel .expandable-content,
  .mod-cashout.small .cashout-button-panel .expandable-content {
    max-width: 100%;
    max-height: 100%;
    margin: 8px 0 0;
  }
  .mod-cashout.mini .cashout-button-panel .auto-cashout-container,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-container,
  .mod-cashout.small .cashout-button-panel .auto-cashout-container {
    max-width: 100%;
    margin: 0;
  }
  .mod-cashout.mini .cashout-button-panel .auto-cashout-button-container,
  .mod-cashout.mini .cashout-button-panel .auto-cashout-label-input-container,
  .mod-cashout.mini .cashout-button-panel .auto-cashout-saved-label-container,
  .mod-cashout.mini .cashout-button-panel .auto-cashout-saved-message-container,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-button-container,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-label-input-container,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-saved-label-container,
  .mod-cashout.narrow
    .cashout-button-panel
    .auto-cashout-saved-message-container,
  .mod-cashout.small .cashout-button-panel .auto-cashout-button-container,
  .mod-cashout.small .cashout-button-panel .auto-cashout-label-input-container,
  .mod-cashout.small .cashout-button-panel .auto-cashout-saved-label-container,
  .mod-cashout.small
    .cashout-button-panel
    .auto-cashout-saved-message-container {
    max-width: 100%;
    margin: 0;
    overflow: hidden;
  }
  .mod-cashout.mini .cashout-button-panel .auto-cashout-label,
  .mod-cashout.mini .cashout-button-panel .auto-cashout-saved-label,
  .mod-cashout.mini .cashout-button-panel .auto-cashout-saved-message-label,
  .mod-cashout.mini .cashout-button-panel .auto-cashout-saved-value,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-label,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-saved-label,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-saved-message-label,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-saved-value,
  .mod-cashout.small .cashout-button-panel .auto-cashout-label,
  .mod-cashout.small .cashout-button-panel .auto-cashout-saved-label,
  .mod-cashout.small .cashout-button-panel .auto-cashout-saved-message-label,
  .mod-cashout.small .cashout-button-panel .auto-cashout-saved-value {
    display: inline-block;
  }
  .mod-cashout.mini .cashout-button-panel .auto-cashout-saved-value,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-saved-value,
  .mod-cashout.small .cashout-button-panel .auto-cashout-saved-value {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-label {
    max-width: 150px;
  }
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-input {
    max-width: 78px;
  }
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-button,
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-saved-label {
    max-width: 190px;
  }
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-saved-message-label {
    max-width: 220px;
  }
  .mod-cashout.narrow .cashout-button-panel .auto-cashout-saved-value {
    max-width: 90px;
  }
  .mod-cashout.mini .auto-cashout-saved-label-container,
  .mod-cashout.small .auto-cashout-saved-label-container {
    display: inline-block;
    width: 100%;
  }
  .mod-cashout.small .cashout-button-panel .cashout-liability {
    max-width: 60px;
  }
  .mod-cashout.small .cashout-button-panel .cashout-button {
    width: 160px;
  }
  .mod-cashout.small .cashout-button-panel .cashout-button-amount-label,
  .mod-cashout.small .cashout-button-panel .cashout-button-profit-label {
    max-width: 60px;
  }
  .mod-cashout.small .cashout-button-panel .cashout-button-amount-value,
  .mod-cashout.small .cashout-button-panel .cashout-button-profit-value {
    max-width: 80px;
  }
  .mod-cashout.small .cashout-button-panel .slider {
    width: 180px;
  }
  .mod-cashout.small
    .cashout-button-panel
    .auto-cashout-label-input-container
    .help-link-container {
    display: inline-block;
  }
  .mod-cashout.small .cashout-button-panel .auto-cashout-label {
    max-width: 160px;
  }
  .mod-cashout.small .cashout-button-panel .auto-cashout-input {
    max-width: 78px;
  }
  .mod-cashout.mini .cashout-button-panel .cashout-button {
    width: 158px;
  }
  .mod-cashout.mini .cashout-button-panel .slider-container {
    display: block;
  }
  .mod-cashout.mini .cashout-button-panel .slider {
    width: 136px;
  }
  .mod-cashout.mini .cashout-button-panel .cashout-tabs-container {
    max-width: 304px;
  }
  .mod-cashout.mini .cashout-button-panel .auto-cashout-label {
    max-width: 135px;
  }
  .mod-cashout.mini .cashout-button-panel .auto-cashout-input {
    max-width: 58px;
  }
  .mod-cashout.mini .cashout-button-panel .auto-cashout-saved-message-label {
    max-width: 200px;
  }
  .mod-cashout.mini .cashout-button-panel .auto-cashout-label-input-container {
    width: auto;
  }
  .mod-cashout .confirmation-panel {
    text-align: center;
  }
  .mod-cashout .confirmation-panel .confirmation-panel-container {
    display: block;
  }
  .mod-cashout .confirmation-panel .cashout-button,
  .mod-cashout .confirmation-panel .cashout-confirmation-cancel-button,
  .mod-cashout .confirmation-panel .confirmation-panel-controls {
    display: inline-block;
    vertical-align: middle;
  }
  .mod-cashout .confirmation-panel .cashout-button {
    width: 240px;
  }
  .mod-cashout .confirmation-panel .cashout-confirmation-cancel-button {
    width: 91px;
  }
  .mod-cashout.narrow .confirmation-panel .cashout-button {
    width: 142px;
  }
  .mod-cashout.mini .confirmation-panel .confirmation-panel-container,
  .mod-cashout.small .confirmation-panel .confirmation-panel-container {
    text-align: center;
  }
  .mod-cashout.mini
    .confirmation-panel
    .cashout-confirmation-message-container.compact-view,
  .mod-cashout.small
    .confirmation-panel
    .cashout-confirmation-message-container.compact-view {
    display: inline-block;
    vertical-align: middle;
  }
  .mod-cashout.small .confirmation-panel .cashout-button {
    width: 210px;
  }
  .mod-cashout.small .confirmation-panel .cashout-confirmation-cancel-button {
    width: 80px;
  }
  .mod-cashout.small
    .confirmation-panel
    .cashout-confirmation-message-container {
    width: 296px;
  }
  .mod-cashout.mini .confirmation-panel .cashout-button {
    width: 40px;
  }
  .mod-cashout.mini .confirmation-panel .cashout-confirmation-cancel-button {
    width: 60px;
  }
  .mod-cashout.mini
    .confirmation-panel
    .cashout-confirmation-message-container {
    width: 208px;
  }
  .mod-cashout .notification-content-container {
    overflow: hidden;
  }
}
.bf-slider {
  width: 100%;
  padding: 0;
  cursor: pointer;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-color: transparent;
  border-radius: 10px;
  margin: 0;
}
.bf-slider[disabled] {
  cursor: default;
}
.bf-slider[disabled]::-webkit-slider-thumb {
  border-color: #e8c87d;
  background-color: #ffda80;
}
.bf-slider[disabled]::-moz-range-progress {
  background-color: #ffda80;
}
.bf-slider[disabled]::-moz-range-thumb {
  border-color: #e8c87d;
  background-color: #ffda80;
}
.bf-slider[disabled]::-ms-fill-lower {
  background-color: #ffda80;
}
.bf-slider[disabled]::-ms-thumb {
  border-color: #e8c87d;
  background-color: #ffda80;
}
.bf-slider:focus {
  outline: 0;
}
.bf-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 16px;
  height: 16px;
  border: 1px solid #e6a40b;
  border-radius: 8px;
  background-color: #ffb80c;
  position: relative;
  top: -3px;
}
.bf-slider::-webkit-slider-runnable-track {
  height: 10px;
}
.bf-slider::-moz-focus-outer {
  border: 0;
}
.bf-slider::-moz-range-thumb {
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 14px;
  height: 14px;
  border: 1px solid #e6a40b;
  border-radius: 8px;
  background-color: #ffb80c;
}
.bf-slider::-moz-range-track {
  height: 10px;
  background-color: #f0f1f5;
  border-radius: 10px;
}
.bf-slider::-moz-range-progress {
  height: 10px;
  background-color: #ffb80c;
  border-radius: 10px;
}
@media screen and (-ms-high-contrast: active), (-ms-high-contrast: none) {
  .bf-slider {
    height: 18px;
  }
}
.bf-slider,
_:-ms-lang(x),
_:-webkit-full-screen {
  height: 18px;
}
.bf-slider::-ms-thumb {
  width: 14px;
  height: 14px;
  border: 1px solid #e6a40b;
  border-radius: 8px;
  background-color: #ffb80c;
}
.bf-slider::-ms-track {
  height: 10px;
  background: 0 0;
  color: transparent;
  border-color: transparent;
  border-radius: 10px;
}
.bf-slider::-ms-fill-lower {
  height: 10px;
  background-color: #ffb80c;
  border-radius: 10px;
}
.bf-slider::-ms-fill-upper {
  height: 10px;
  background-color: #f0f1f5;
  border-radius: 10px;
}
.bf-slider::-ms-tooltip {
  display: none;
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
.bf-bet-button {
  font-family: Tahoma, Verdana, Arial, sans-serif;
  font-size: 11px;
  width: 100%;
  height: 100%;
  border-width: 0;
  background-color: #fff;
  outline: 0;
  cursor: pointer;
}
.bf-bet-button.changed {
  -webkit-animation-name: highlightDefault;
  -webkit-animation-duration: 0.3s;
  -moz-animation-name: highlightDefault;
  -moz-animation-duration: 0.3s;
  -ms-animation-name: highlightDefault;
  -ms-animation-duration: 0.3s;
  animation-name: highlightDefault;
  animation-duration: 0.3s;
}
.bf-bet-button.selected {
  box-shadow: inset 0 0 6px 0 rgba(127, 127, 127, 0.8);
}
.bf-bet-button:hover {
  background-color: #dfdfdf;
}
.bf-bet-button .bet-button-price,
.bf-bet-button .bet-button-size,
.bf-bet-button .sp-label {
  text-align: center;
  display: block;
}
.bf-bet-button .bet-button-price,
.bf-bet-button .sp-label {
  font-weight: 700;
}
.bf-bet-button.back-button.is-sp,
.bf-bet-button.back-selection-button {
  background-color: #a6d8ff;
}
.bf-bet-button.back-button.is-sp:hover,
.bf-bet-button.back-selection-button:hover {
  background-color: #75c2fd;
}
.bf-bet-button.back-button.is-sp.back-button-empty,
.bf-bet-button.back-selection-button.back-button-empty {
  background-color: #e7eff5;
}
.bf-bet-button.lay-button.is-sp,
.bf-bet-button.lay-selection-button {
  background-color: #fac9d1;
}
.bf-bet-button.lay-button.is-sp:hover,
.bf-bet-button.lay-selection-button:hover {
  background-color: #f694aa;
}
.bf-bet-button.lay-button.is-sp.lay-button-empty,
.bf-bet-button.lay-selection-button.lay-button-empty {
  background-color: #f4e7e9;
}
.bf-livescores {
  font-family: Arial, Helvetica, sans-serif;
}
.bf-livescores * {
  box-sizing: border-box;
  line-height: inherit;
  outline: 0;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.bf-livescores.full {
  width: 100%;
  min-width: 320px;
  background-color: #424242;
}
.bf-livescores.full .default-template .results-board {
  height: 48px;
}
.bf-livescores.full .default-template .results-board .bf-livescores-runners {
  padding: 8px 10px 8px 0;
}
.bf-livescores.full
  .default-template
  .results-board
  .bf-livescores-runners
  .runner {
  padding-left: 10px;
}
.bf-livescores.full
  .default-template
  .results-board
  .bf-livescores-runners.showing-turns {
  padding-left: 4px;
}
.bf-livescores.full
  .default-template
  .results-board
  .bf-livescores-runners.showing-turns
  .runner {
  padding-left: 0;
}
.bf-livescores.full
  .default-template
  .results-board
  .bf-livescores-time-elapsed {
  border-right: 1px solid #000;
  float: left;
  width: 35px;
}
.bf-livescores.full .default-template .results-board .bf-livescores-start-date {
  float: right;
}
.bf-livescores.full .default-template .results-board .bf-livescores-innings {
  float: right;
  padding-right: 10px;
  padding-left: 5px;
}
.bf-livescores.full
  .default-template
  .results-board
  .bf-livescores-match-scores {
  float: right;
}
.bf-livescores.full
  .default-template
  .results-board
  .bf-livescores-scores
  .bf-livescores-match-scores {
  float: none;
  margin-right: 1px;
}
.bf-livescores.full .default-template .results-board .bf-livescores-scores {
  display: inline;
  float: right;
  padding-right: 10px;
  padding-left: 5px;
}
.bf-livescores.full .default-template .bf-livescores-additional-info {
  border-top: 1px solid #fff;
}
.bf-livescores.full .default-template.football .bf-livescores-time-elapsed,
.bf-livescores.full .default-template.handball .bf-livescores-time-elapsed,
.bf-livescores.full
  .default-template.ice-hockey.penalties
  .bf-livescores-time-elapsed {
  border-width: 0;
}
.bf-livescores.full .default-template.football .bf-livescores-match-scores,
.bf-livescores.full .default-template.handball .bf-livescores-match-scores,
.bf-livescores.full
  .default-template.ice-hockey.penalties
  .bf-livescores-match-scores {
  float: left;
}
.bf-livescores.full
  .default-template.football.penalties
  .bf-livescores-additional-info,
.bf-livescores.full
  .default-template.football.timeline
  .bf-livescores-additional-info,
.bf-livescores.full
  .default-template.handball.penalties
  .bf-livescores-additional-info,
.bf-livescores.full
  .default-template.handball.timeline
  .bf-livescores-additional-info,
.bf-livescores.full
  .default-template.ice-hockey.penalties.penalties
  .bf-livescores-additional-info,
.bf-livescores.full
  .default-template.ice-hockey.penalties.timeline
  .bf-livescores-additional-info {
  height: 21px;
  line-height: 21px;
}
.bf-livescores.full
  .default-template.football.penalties
  .bf-livescores-additional-info-scores,
.bf-livescores.full
  .default-template.football.timeline
  .bf-livescores-additional-info-scores,
.bf-livescores.full
  .default-template.handball.penalties
  .bf-livescores-additional-info-scores,
.bf-livescores.full
  .default-template.handball.timeline
  .bf-livescores-additional-info-scores,
.bf-livescores.full
  .default-template.ice-hockey.penalties.penalties
  .bf-livescores-additional-info-scores,
.bf-livescores.full
  .default-template.ice-hockey.penalties.timeline
  .bf-livescores-additional-info-scores {
  font-size: 11px;
}
.bf-livescores.mini {
  display: inline-block;
}
.bf-livescores.mini .default-template {
  width: 42px;
  height: 60px;
}
.bf-livescores.mini .default-template .bf-livescores-time-elapsed {
  width: 25px;
  float: left;
}
.bf-livescores.mini .default-template.volleyball {
  width: 60px;
}
.bf-livescores.mini .default-template.darts {
  width: 60px;
  height: 46px;
}
.bf-livescores.coupon .default-template {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  height: 60px;
  background-color: #fff;
}
.bf-livescores.coupon .default-template .mini-coupon {
  display: -ms-flexbox;
  display: flex;
  width: 42px;
  min-width: 42px;
  height: 100%;
  font-size: 10px;
  line-height: 13px;
}
.bf-livescores.coupon .default-template .bf-livescores-extended-scores,
.bf-livescores.coupon .default-template .bf-livescores-innings,
.bf-livescores.coupon .default-template .bf-livescores-match-scores,
.bf-livescores.coupon .default-template .bf-livescores-start-date,
.bf-livescores.coupon .default-template .bf-livescores-time-elapsed {
  height: 60px;
}
.bf-livescores.coupon .default-template .bf-livescores-time-elapsed {
  width: 25px;
}
.bf-livescores.coupon .default-template .bf-livescores-start-date {
  width: 42px;
}
.bf-livescores.coupon .default-template .right-content {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  margin-left: 10px;
  min-width: 0;
}
.bf-livescores.coupon .default-template .event-info-content {
  display: -ms-flexbox;
  display: flex;
  line-height: 12px;
  -ms-flex-align: center;
  align-items: center;
}
.bf-livescores.coupon .default-template .bf-livescores-info-label {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 2px;
}
.bf-livescores.coupon
  .default-template.has-broadcasts-icons
  .bf-livescores-extended-scores
  .cell,
.bf-livescores.coupon
  .default-template.has-broadcasts-icons
  .bf-livescores-innings
  .current-inning,
.bf-livescores.coupon
  .default-template.has-broadcasts-icons
  .bf-livescores-match-scores
  .scores,
.bf-livescores.coupon
  .default-template.has-broadcasts-icons
  .bf-livescores-time-elapsed
  .cell,
.bf-livescores.coupon
  .default-template.has-info-label
  .bf-livescores-extended-scores
  .cell,
.bf-livescores.coupon
  .default-template.has-info-label
  .bf-livescores-innings
  .current-inning,
.bf-livescores.coupon
  .default-template.has-info-label
  .bf-livescores-match-scores
  .scores,
.bf-livescores.coupon
  .default-template.has-info-label
  .bf-livescores-time-elapsed
  .cell {
  padding-top: 9px;
  vertical-align: text-top;
}
.bf-livescores-additional-info {
  color: #fff;
  font-size: 12px;
  height: 30px;
  line-height: 30px;
  padding: 0 10px;
  width: 100%;
  background-color: #1e1e1e;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.bf-livescores-innings {
  display: table;
  color: #fff;
  height: 100%;
}
.bf-livescores-innings .inning {
  display: table-cell;
  padding: 0 5px;
  background-color: #303030;
  font-weight: 700;
  vertical-align: middle;
}
.bf-livescores-innings .inning:first-child {
  border-right: solid 1px #303030;
}
.coupon .bf-livescores-innings,
.mini .bf-livescores-innings {
  display: inline-table;
  width: 42px;
  background-color: #4b4b4b;
}
.coupon .bf-livescores-innings.in-play,
.mini .bf-livescores-innings.in-play {
  background-color: #20a052;
}
.coupon .bf-livescores-innings .current-inning,
.mini .bf-livescores-innings .current-inning {
  margin: 0 auto;
  display: table-cell;
  vertical-align: middle;
  text-align: center;
  font-weight: 700;
}
.coupon .bf-livescores-innings .current-inning .away,
.coupon .bf-livescores-innings .current-inning .home,
.mini .bf-livescores-innings .current-inning .away,
.mini .bf-livescores-innings .current-inning .home {
  width: 100%;
}
.mini .bf-livescores-innings {
  font-size: 10px;
  line-height: 14px;
}
.bf-livescores-innings .highlight {
  color: #20a052;
}
.bf-livescores-innings .unplayed {
  color: #9f9f9f;
  padding: 0 35px;
}
.bf-livescores-innings .away,
.bf-livescores-innings .home {
  white-space: nowrap;
  overflow: hidden;
  width: 84px;
}
.bf-livescores-innings .over-tries,
.bf-livescores-innings .run-wickets-dec {
  font-size: 10px;
}
.full .bf-livescores-innings {
  font-size: 12px;
  line-height: 17px;
}
.bf-livescores-innings .run-wickets-dec {
  font-size: 10px;
}
.bf-livescores-broadcasts-icons {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  height: 12px;
  margin-top: 2px;
}
.bf-livescores-broadcasts-icons .live-video,
.bf-livescores-broadcasts-icons .on-tv {
  margin-right: 4px;
}
.bf-livescores-extended-scores {
  display: inline-table;
  font-weight: 700;
  height: 100%;
}
.full .bf-livescores-extended-scores {
  color: #9d9d9d;
  font-size: 12px;
  line-height: 19px;
}
.full .bf-livescores-extended-scores .darts,
.full .bf-livescores-extended-scores .points,
.full .bf-livescores-extended-scores .sequence,
.full .bf-livescores-extended-scores .snooker {
  background-color: #303030;
  display: inline-table;
  min-width: 16px;
  height: 100%;
}
.full .bf-livescores-extended-scores .quarter {
  display: inline-block;
  width: 20px;
}
.full .bf-livescores-extended-scores .sequence .quarter:first-child {
  margin-left: 5px;
}
.full .bf-livescores-extended-scores .sequence .quarter:last-child {
  margin-right: 5px;
}
.full .bf-livescores-extended-scores .sequence .active {
  color: #fff;
}
.full .bf-livescores-extended-scores .points {
  margin-left: 1px;
  width: 30px;
}
.full .bf-livescores-extended-scores .points .active {
  color: #20a052;
}
.full .bf-livescores-extended-scores .points .quarter:first-child {
  margin-left: 0;
}
.full .bf-livescores-extended-scores .points .quarter:last-child {
  margin-right: 0;
}
.full .bf-livescores-extended-scores .cell {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}
.full .bf-livescores-extended-scores .darts,
.full .bf-livescores-extended-scores .snooker {
  margin-right: 1px;
}
.full .bf-livescores-extended-scores .darts .cell,
.full .bf-livescores-extended-scores .snooker .cell {
  width: 25px;
  height: 48px;
}
.full .bf-livescores-extended-scores .darts.points,
.full .bf-livescores-extended-scores .snooker.points {
  width: 43px;
  margin-left: 0;
}
.full .bf-livescores-extended-scores .darts.points .active,
.full .bf-livescores-extended-scores .snooker.points .active {
  color: #fff;
}
.full .bf-livescores-extended-scores .darts.legs {
  color: #9d9d9d;
}
.full .bf-livescores-extended-scores .darts.legs .active {
  color: #fff;
}
.coupon .full .bf-livescores-extended-scores .snooker.points,
.full .bf-livescores-extended-scores .snooker.games,
.full .coupon .bf-livescores-extended-scores .snooker.points,
.full .mini .bf-livescores-extended-scores .snooker.points,
.mini .full .bf-livescores-extended-scores .snooker.points {
  margin-left: 0;
}
.coupon .full .bf-livescores-extended-scores .snooker.points .active,
.full .bf-livescores-extended-scores .snooker.games .active,
.full .coupon .bf-livescores-extended-scores .snooker.points .active,
.full .mini .bf-livescores-extended-scores .snooker.points .active,
.mini .full .bf-livescores-extended-scores .snooker.points .active {
  color: #20a052;
}
.coupon .full .bf-livescores-extended-scores .snooker.points .finished,
.full .bf-livescores-extended-scores .snooker.games .finished,
.full .coupon .bf-livescores-extended-scores .snooker.points .finished,
.full .mini .bf-livescores-extended-scores .snooker.points .finished,
.mini .full .bf-livescores-extended-scores .snooker.points .finished {
  color: #fff;
}
.coupon .bf-livescores-extended-scores .games,
.coupon .bf-livescores-extended-scores .snooker.points,
.mini .bf-livescores-extended-scores .games,
.mini .bf-livescores-extended-scores .snooker.points {
  display: table;
  width: 21px;
  color: #fff;
  height: 100%;
}
.coupon .bf-livescores-extended-scores .games .cell,
.coupon .bf-livescores-extended-scores .snooker.points .cell,
.mini .bf-livescores-extended-scores .games .cell,
.mini .bf-livescores-extended-scores .snooker.points .cell {
  display: table-cell;
  background-color: #20a052;
  padding: 0;
  vertical-align: middle;
  text-align: center;
}
.coupon .bf-livescores-extended-scores .snooker.points,
.mini .bf-livescores-extended-scores .snooker.points {
  background-color: #4db375;
  width: 21px;
}
.mini .bf-livescores-extended-scores {
  font-size: 10px;
  line-height: 14px;
}
.mini .bf-livescores-extended-scores .darts.games,
.mini .bf-livescores-extended-scores .darts.snooker.points {
  width: 30px;
  font-size: 12px;
}
.coupon .bf-livescores-extended-scores .darts.games,
.coupon .bf-livescores-extended-scores .darts.snooker.points {
  width: 25px;
}
.info-label {
  color: #303030;
  font-weight: 400;
  font-size: 11px;
}
.bf-livescores-match-scores {
  display: inline-table;
  color: #fff;
  height: 100%;
}
.bf-livescores-match-scores .scores {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
  font-weight: 700;
}
.bf-livescores-match-scores .away,
.bf-livescores-match-scores .home {
  display: block;
}
.full .bf-livescores-match-scores {
  font-size: 12px;
  line-height: 19px;
  background-color: #303030;
}
.full .bf-livescores-match-scores.in-play {
  color: #20a052;
}
.full .bf-livescores-match-scores .scores {
  width: 30px;
}
.coupon .bf-livescores-match-scores,
.mini .bf-livescores-match-scores {
  background-color: #20a052;
}
.coupon .bf-livescores-match-scores.finished,
.mini .bf-livescores-match-scores.finished {
  background-color: #4b4b4b;
}
.coupon .bf-livescores-match-scores .scores,
.mini .bf-livescores-match-scores .scores {
  width: 17px;
}
.mini .bf-livescores-match-scores {
  font-size: 10px;
  line-height: 14px;
}
.coupon .darts .bf-livescores-match-scores,
.coupon .snooker .bf-livescores-match-scores,
.coupon .tennis .bf-livescores-match-scores,
.coupon .volleyball .bf-livescores-match-scores,
.mini .darts .bf-livescores-match-scores,
.mini .snooker .bf-livescores-match-scores,
.mini .tennis .bf-livescores-match-scores,
.mini .volleyball .bf-livescores-match-scores {
  background-color: #4db375;
}
.coupon .darts .bf-livescores-match-scores.finished,
.coupon .snooker .bf-livescores-match-scores.finished,
.coupon .tennis .bf-livescores-match-scores.finished,
.coupon .volleyball .bf-livescores-match-scores.finished,
.mini .darts .bf-livescores-match-scores.finished,
.mini .snooker .bf-livescores-match-scores.finished,
.mini .tennis .bf-livescores-match-scores.finished,
.mini .volleyball .bf-livescores-match-scores.finished {
  background-color: #4b4b4b;
}
.coupon .snooker .bf-livescores-match-scores.in-play,
.coupon .tennis .bf-livescores-match-scores.in-play,
.coupon .volleyball .bf-livescores-match-scores.in-play,
.mini .snooker .bf-livescores-match-scores.in-play,
.mini .tennis .bf-livescores-match-scores.in-play,
.mini .volleyball .bf-livescores-match-scores.in-play {
  width: 21px;
}
.mini .darts .bf-livescores-match-scores .scores {
  width: 30px;
  font-size: 12px;
}
.bf-livescores-penalties {
  display: inline-table;
  background-color: #1e1e1e;
  padding: 7px 10px;
  width: 100%;
}
.bf-livescores-penalties .runner {
  display: table-cell;
  vertical-align: middle;
}
.bf-livescores-penalties .runner .icon {
  border-radius: 100%;
  height: 11px;
  width: 11px;
}
.bf-livescores-penalties .runner .icon.empty {
  height: 11px;
  width: 11px;
  border: 1px solid #7f7f7f;
}
.bf-livescores-penalties .runner.home .icon {
  float: left;
  margin-right: 5px;
}
.bf-livescores-penalties .runner.away {
  float: right;
}
.bf-livescores-penalties .runner.away .icon {
  float: left;
  margin-left: 5px;
}
.bf-livescores-penalties .score {
  color: #20a052;
  display: table-cell;
  font-size: 13px;
  font-weight: 700;
  text-align: center;
  vertical-align: middle;
  width: 20%;
}
.bf-livescores-penalties .score .score-element {
  padding: 0 5px;
  display: inline-block;
}
.bf-livescores-penalties .score .taker-indicator {
  background-color: #20a052;
  border-radius: 100%;
  display: inline-block;
  height: 5px;
  width: 5px;
  margin-bottom: 2px;
}
.bf-livescores-runners {
  color: #fff;
  font-weight: 700;
  font-size: 12px;
  line-height: 17px;
}
.bf-livescores-runners .runner {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  position: relative;
}
.bf-livescores-runners .bullet {
  position: absolute;
  margin: 7px 5px 2px;
  width: 4px;
  height: 4px;
  border-radius: 2px;
  left: 0;
  top: 0;
}
.bf-livescores-runners .highlight {
  background-color: #20a052;
}
.bf-livescores-runners .loser {
  color: #9d9d9d;
}
.bf-livescores-runners.showing-turns .name {
  padding-left: 18px;
}
.bf-livescores-runners .name.reversed::before {
  content: "@ ";
}
.bf-livescores-runners .showing-seed .name {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  float: left;
}
.bf-livescores-runners .showing-seed .player-seed {
  display: inline-block;
}
.bf-livescores-runners .showing-seed .player-seed:before {
  content: "\00a0";
}
.bf-livescores-runners .showing-seed.seed-with-1-digits .name {
  max-width: calc(100% - 20px);
}
.bf-livescores-runners .showing-seed.seed-with-1-digits .player-seed {
  width: 20px;
}
.bf-livescores-runners .showing-seed.seed-with-2-digits .name {
  max-width: calc(100% - 30px);
}
.bf-livescores-runners .showing-seed.seed-with-2-digits .player-seed {
  width: 30px;
}
.bf-livescores-runners .showing-seed.seed-with-3-digits .name {
  max-width: calc(100% - 40px);
}
.bf-livescores-runners .showing-seed.seed-with-3-digits .player-seed {
  width: 40px;
}
.bf-livescores-runners .showing-seed.seed-with-4-digits .name {
  max-width: calc(100% - 50px);
}
.bf-livescores-runners .showing-seed.seed-with-4-digits .player-seed {
  width: 50px;
}
.coupon .bf-livescores-runners {
  color: #303030;
  font-weight: 400;
  font-size: 11px;
  line-height: 13px;
}
.coupon .bf-livescores-runners .bullet {
  margin: 5px 0 0 4px;
}
.coupon .bf-livescores-runners .loser {
  color: #7f7f7f;
}
.full .bf-livescores-scores {
  height: 48px;
}
.mini .bf-livescores-scores {
  height: 60px;
}
.full .bf-livescores-scores .bf-livescores-match-scores {
  margin-right: 1px;
}
.coupon .bf-livescores-scores .bf-livescores-match-scores.in-play,
.mini .bf-livescores-scores .bf-livescores-match-scores.in-play {
  background-color: #4db375;
}
.coupon .bf-livescores-scores .bf-livescores-match-scores .scores,
.mini .bf-livescores-scores .bf-livescores-match-scores .scores {
  width: 21px;
}
.bf-livescores-start-date {
  display: inline-table;
  height: 100%;
}
.bf-livescores-start-date .start-date-wrapper {
  display: table-cell;
  text-align: right;
  vertical-align: middle;
  overflow: hidden;
  text-overflow: ellipsis;
}
.full .bf-livescores-start-date {
  padding: 8px 10px;
  font-size: 12px;
  line-height: 13px;
  color: #fff;
}
.full .bf-livescores-start-date.in-play {
  color: #20a052;
}
.coupon .bf-livescores-start-date,
.mini .bf-livescores-start-date {
  padding: 0 2px;
  color: #7f7f7f;
  background-color: #f6f6f6;
  width: 100%;
}
.coupon .bf-livescores-start-date .start-date-wrapper,
.mini .bf-livescores-start-date .start-date-wrapper {
  max-width: 38px;
  text-align: center;
}
.coupon .bf-livescores-start-date.in-play,
.mini .bf-livescores-start-date.in-play {
  color: #fff;
  background-color: #20a052;
}
.mini .bf-livescores-start-date {
  font-size: 10px;
  line-height: 14px;
}
.bf-livescores-timeline-bar {
  background-color: #fff;
  position: relative;
  width: 100%;
  height: 5px;
}
.bf-livescores-timeline-bar .event-item {
  position: absolute;
  transform: translateX(-5px);
  top: -10px;
}
.bf-livescores-timeline-bar .event-item.away {
  top: 3px;
}
.bf-livescores-timeline-bar .elapsed-time {
  background-color: #20a052;
  height: 5px;
  top: 0;
  left: 0;
  width: 0;
}
.event-tooltip {
  position: relative;
}
.event-tooltip .tooltip-text {
  display: none;
  padding: 4px;
  color: #1e1e1e;
  background-color: #fff;
  border-radius: 2px;
  font-size: 11px;
  white-space: nowrap;
  position: absolute;
  left: -6px;
  top: 19px;
  z-index: 1;
}
.event-tooltip .tooltip-text .icon {
  display: inline-block;
  margin-right: 3px;
  margin-bottom: -2px;
}
.event-tooltip .tooltip-text .icon.yellow-red-card {
  margin-bottom: -4px;
}
.event-tooltip .home .tooltip-text {
  top: -28px;
}
.event-tooltip .home.goal .tooltip-text {
  left: -4px;
}
.event-tooltip .home .tooltip-text::after {
  content: " ";
  position: absolute;
  top: 100%;
  left: 6px;
  border-width: 4px;
  border-style: solid;
  border-color: #fff transparent transparent;
}
.event-tooltip .away .tooltip-text::after {
  content: " ";
  position: absolute;
  bottom: 100%;
  left: 6px;
  border-width: 4px;
  border-style: solid;
  border-color: transparent transparent #fff;
}
.event-tooltip:hover .tooltip-text {
  display: block;
}
.bf-livescores-timeline {
  background-color: #1e1e1e;
  height: 30px;
  padding: 4px 10px;
}
.bf-livescores-timeline .extra-time,
.bf-livescores-timeline .regular-time {
  display: inline-block;
}
.bf-livescores-timeline .regular-time {
  width: 100%;
}
.bf-livescores-timeline .regular-time.has-et {
  width: 66%;
  padding-right: 10px;
}
.bf-livescores-timeline .extra-time {
  width: 34%;
}
.bf-livescores-timeline .first-half,
.bf-livescores-timeline .second-half {
  display: inline-block;
  width: 50%;
}
.bf-livescores-timeline .first-half {
  padding-right: 3px;
}
.bf-livescores-timeline .second-half {
  padding: 0;
}
.bf-livescores-time-elapsed {
  display: inline-table;
  height: 100%;
}
.bf-livescores-time-elapsed .cell {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
  font-weight: 700;
}
.top .bf-livescores-time-elapsed .cell {
  padding-top: 12px;
  vertical-align: top;
}
.bf-livescores-time-elapsed .top-label {
  margin-bottom: 2px;
}
.full .bf-livescores-time-elapsed {
  color: #20a052;
  font-size: 12px;
  line-height: 12px;
}
.full .bf-livescores-time-elapsed .cell {
  height: 32px;
}
.full .bf-livescores-time-elapsed .finished {
  color: #fff;
}
.full .bf-livescores-time-elapsed .bottom-label,
.full .bf-livescores-time-elapsed .top-label {
  font-size: 10px;
  line-height: 10px;
}
.coupon .bf-livescores-time-elapsed,
.mini .bf-livescores-time-elapsed {
  color: #fff;
  background-color: #4db375;
}
.coupon .bf-livescores-time-elapsed .top-label,
.mini .bf-livescores-time-elapsed .top-label {
  margin-bottom: 4px;
}
.coupon .bf-livescores-time-elapsed .cell,
.mini .bf-livescores-time-elapsed .cell {
  margin: 0 auto;
  max-width: 25px;
}
.coupon .bf-livescores-time-elapsed .bottom-label,
.mini .bf-livescores-time-elapsed .bottom-label {
  margin-top: 4px;
}
.coupon .bf-livescores-time-elapsed .finished,
.mini .bf-livescores-time-elapsed .finished {
  background-color: #787878;
}
.coupon .bf-livescores-time-elapsed .bottom-label,
.coupon .bf-livescores-time-elapsed .middle-label,
.coupon .bf-livescores-time-elapsed .top-label,
.mini .bf-livescores-time-elapsed .bottom-label,
.mini .bf-livescores-time-elapsed .middle-label,
.mini .bf-livescores-time-elapsed .top-label {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.mini .bf-livescores-time-elapsed {
  font-size: 10px;
  line-height: 10px;
}
.coupon .bf-livescores-time-elapsed .bottom-label,
.coupon .bf-livescores-time-elapsed .top-label {
  margin: 0;
}
.seo-footer {
  font-family: Arial, Helvetica, sans-serif;
  color: #303030;
  background-color: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2);
  padding: 12px 10px 1px;
}
.seo-footer__title {
  font-size: 12px;
  font-weight: 700;
  margin: 4px 0 0;
}
.seo-footer__description {
  font-size: 12px;
  margin: 12px 0;
  line-height: 14px;
}
.seo-footer__description a {
  font-weight: 700;
  color: #167ac6;
  text-decoration: none;
}
.seo-footer__description a:hover {
  text-decoration: underline;
}
@keyframes ngdialog-fadeout {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
@keyframes ngdialog-fadein {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
.ngdialog {
  box-sizing: border-box;
}
.ngdialog *,
.ngdialog :after,
.ngdialog :before {
  box-sizing: inherit;
}
.ngdialog {
  position: fixed;
  overflow: auto;
  -webkit-overflow-scrolling: touch;
  z-index: 10000;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
.ngdialog.ngdialog-disabled-animation,
.ngdialog.ngdialog-disabled-animation .ngdialog-content,
.ngdialog.ngdialog-disabled-animation .ngdialog-overlay {
  animation: none !important;
}
.ngdialog-overlay {
  position: fixed;
  background: rgba(0, 0, 0, 0.4);
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  -webkit-backface-visibility: hidden;
  animation: ngdialog-fadein 0.5s;
}
.ngdialog-no-overlay {
  pointer-events: none;
}
.ngdialog.ngdialog-closing .ngdialog-overlay {
  -webkit-backface-visibility: hidden;
  animation: ngdialog-fadeout 0.5s;
}
.ngdialog-content {
  background: #fff;
  -webkit-backface-visibility: hidden;
  animation: ngdialog-fadein 0.5s;
  pointer-events: all;
}
.ngdialog.ngdialog-closing .ngdialog-content {
  -webkit-backface-visibility: hidden;
  animation: ngdialog-fadeout 0.5s;
}
.ngdialog-close {
  -webkit-appearance: none;
  background: 0 0;
  border: 0;
}
.ngdialog-close:before {
  font-family: Helvetica, Arial, sans-serif;
  content: "\00D7";
  cursor: pointer;
}
body.ngdialog-open,
html.ngdialog-open {
  overflow: hidden;
}
@keyframes ngdialog-flyin {
  0% {
    opacity: 0;
    transform: translateY(-40px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes ngdialog-flyout {
  0% {
    opacity: 1;
    transform: translateY(0);
  }
  100% {
    opacity: 0;
    transform: translateY(-40px);
  }
}
.ngdialog.ngdialog-theme-default {
  padding-bottom: 160px;
  padding-top: 160px;
}
.ngdialog.ngdialog-theme-default.ngdialog-closing .ngdialog-content {
  animation: ngdialog-flyout 0.5s;
}
.ngdialog.ngdialog-theme-default .ngdialog-content {
  animation: ngdialog-flyin 0.5s;
  background: #f0f0f0;
  border-radius: 5px;
  color: #444;
  font-family: Helvetica, sans-serif;
  font-size: 1.1em;
  line-height: 1.5em;
  margin: 0 auto;
  max-width: 100%;
  padding: 1em;
  position: relative;
  width: 450px;
}
.ngdialog.ngdialog-theme-default .ngdialog-close {
  border-radius: 5px;
  cursor: pointer;
  position: absolute;
  right: 0;
  top: 0;
}
.ngdialog.ngdialog-theme-default .ngdialog-close:before {
  background: 0 0;
  border-radius: 3px;
  color: #bbb;
  content: "\00D7";
  font-size: 26px;
  font-weight: 400;
  height: 30px;
  line-height: 26px;
  position: absolute;
  right: 3px;
  text-align: center;
  top: 3px;
  width: 30px;
}
.ngdialog.ngdialog-theme-default .ngdialog-close:active:before,
.ngdialog.ngdialog-theme-default .ngdialog-close:hover:before {
  color: #777;
}
.ngdialog.ngdialog-theme-default .ngdialog-message {
  margin-bottom: 0.5em;
}
.ngdialog.ngdialog-theme-default .ngdialog-input {
  margin-bottom: 1em;
}
.ngdialog.ngdialog-theme-default .ngdialog-input input[type="email"],
.ngdialog.ngdialog-theme-default .ngdialog-input input[type="password"],
.ngdialog.ngdialog-theme-default .ngdialog-input input[type="text"],
.ngdialog.ngdialog-theme-default .ngdialog-input input[type="url"],
.ngdialog.ngdialog-theme-default .ngdialog-input textarea {
  background: #fff;
  border: 0;
  border-radius: 3px;
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  margin: 0 0 0.25em;
  min-height: 2.5em;
  padding: 0.25em 0.67em;
  width: 100%;
}
.ngdialog.ngdialog-theme-default .ngdialog-input input[type="email"]:focus,
.ngdialog.ngdialog-theme-default .ngdialog-input input[type="password"]:focus,
.ngdialog.ngdialog-theme-default .ngdialog-input input[type="text"]:focus,
.ngdialog.ngdialog-theme-default .ngdialog-input input[type="url"]:focus,
.ngdialog.ngdialog-theme-default .ngdialog-input textarea:focus {
  box-shadow: inset 0 0 0 2px #8dbdf1;
  outline: 0;
}
.ngdialog.ngdialog-theme-default .ngdialog-buttons {
  *zoom: 1;
}
.ngdialog.ngdialog-theme-default .ngdialog-buttons:after {
  content: "";
  display: table;
  clear: both;
}
.ngdialog.ngdialog-theme-default .ngdialog-button {
  border: 0;
  border-radius: 3px;
  cursor: pointer;
  float: right;
  font-family: inherit;
  font-size: 0.8em;
  letter-spacing: 0.1em;
  line-height: 1em;
  margin: 0 0 0 0.5em;
  padding: 0.75em 2em;
  text-transform: uppercase;
}
.ngdialog.ngdialog-theme-default .ngdialog-button:focus {
  animation: ngdialog-pulse 1.1s infinite;
  outline: 0;
}
@media (max-width: 568px) {
  .ngdialog.ngdialog-theme-default .ngdialog-button:focus {
    animation: none;
  }
}
.ngdialog.ngdialog-theme-default .ngdialog-button.ngdialog-button-primary {
  background: #3288e6;
  color: #fff;
}
.ngdialog.ngdialog-theme-default .ngdialog-button.ngdialog-button-secondary {
  background: #e0e0e0;
  color: #777;
}
.runner-timeform-wrapper__runner-info {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 10px 0;
}
.runner-timeform-wrapper__horse-details {
  min-width: 54%;
}
.runner-timeform-wrapper__details {
  line-height: normal;
  padding-bottom: 4px;
}
.runner-timeform-wrapper__details-strong {
  font-weight: 700;
}
.runner-timeform-wrapper__age-weight-rating-strong:not(:first-child) {
  margin-left: 20px;
}
.runner-timeform-wrapper__horse-comments
  .runner-timeform-wrapper__details:last-child {
  padding-bottom: 0;
}
@media screen and (min-width: 490px) {
  .runner-timeform-wrapper__runner-info {
    -ms-flex-wrap: nowrap;
    flex-wrap: nowrap;
  }
}
@media (-ms-high-contrast: active), (-ms-high-contrast: none) {
  .runner-timeform-wrapper__horse-comments {
    max-width: 46%;
  }
}
.runner-past-races__row {
  max-width: 100%;
  display: -ms-flexbox;
  display: flex;
  height: 38px;
  line-height: 38px;
  overflow: hidden;
  -ms-flex-pack: justify;
  justify-content: space-between;
  border-bottom: 1px solid #ebebeb;
}
.runner-past-races__row:first-child {
  border-top: 1px solid #ebebeb;
  border-bottom: 0;
}
.runner-past-races__row--header {
  font-weight: 700;
}
.runner-past-races__columns-body {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  -ms-flex-pack: justify;
  justify-content: space-between;
  width: 100%;
}
.runner-past-races__column {
  width: 120px;
  line-height: 38px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-align: center;
}
.runner-past-races__column--date {
  width: 66px;
  text-align: left;
}
.runner-past-races__column--course {
  font-weight: 700;
}
.runner-past-races__column--course-full,
.runner-past-races__column--type-full {
  display: none;
}
.runner-past-races__column--course,
.runner-past-races__column--distance,
.runner-past-races__column--hi-lo,
.runner-past-races__column--position {
  width: 55px;
}
.runner-past-races__column--course {
  width: 45px;
}
.runner-past-races__column--type {
  width: 30px;
}
.runner-past-races__column--going {
  width: 44px;
}
.runner-past-races__column--or {
  width: 34px;
}
.runner-past-races__column--bsp {
  width: 39px;
}
.runner-past-races__column--jockey {
  width: 156px;
}
.runner-past-races__column--course,
.runner-past-races__column--jockey {
  text-align: left;
}
.runner-past-races__column--type {
  text-align: center;
}
.runner-past-races__column--av {
  padding-top: 11px;
  line-height: 0;
  width: 32px;
  text-align: right;
}
.runner-past-races__av-svg {
  width: 22px;
  height: 16px;
  cursor: pointer;
}
.runner-past-races__row-av {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: center;
  justify-content: center;
}
.runner-past-races__row-av-iframe-wrapper {
  position: absolute;
  overflow: hidden;
  top: -99999px;
}
.runner-past-races__row-av-iframe {
  overflow: hidden;
  border: 0;
  transform-origin: top left;
}
@media screen and (min-width: 766px) {
  .runner-past-races__column--course,
  .runner-past-races__column--type {
    width: 100px;
  }
  .runner-past-races__column--distance {
    width: 80px;
  }
  .runner-past-races__column--course-abbr,
  .runner-past-races__column--type-abbr {
    display: none;
  }
  .runner-past-races__column--course-full,
  .runner-past-races__column--type-full {
    display: block;
  }
}
@media (-ms-high-contrast: active), (-ms-high-contrast: none) {
  .runner-past-races__columns-body {
    max-width: 87%;
  }
  .runner-past-races__column.runner-past-races__column--av {
    text-align: left;
  }
}
.runner-timeform-wrapper {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 11px;
  background-color: #fff;
  color: #303030;
}
.ladder-table {
  display:block;
  border-collapse:collapse;
  overflow-y:auto;
  overflow-x:hidden;
  max-height:644px;
  border:1px solid #F0F1F5;
  font:normal normal normal 12px "Arial","sans-serif";
}
.ladder-table thead {
  display:table;
  width:100%
}
.ladder-table th {
  height:18px;
  padding:5px;
  text-align:center;
  font:normal normal bold 12px "Arial","sans-serif";
}
.ladder-table .titles th {
  background-color:#F0F1F5
}
.ladder-table tbody tr {
  display: table;
  width: 100%;
  table-layout:fixed
}
.ladder-table td {
  padding:5px;
  font:normal normal normal 12px "Arial","sans-serif";
  border:1px solid #DFDFDf;
  border-bottom:0;
  height:14px
}
.ladder-table .item td .price {
  text-align:left
}
.ladder-table .item td.price.back-color,
.ladder-table .item td.back.back-color {
  background-color:#A6D8FF
}
.ladder-table .item td.price.lay-color,
.ladder-table .item td.lay.lay-color {
  background-color:#FAC9D1
}
.ladder-table .item td.back,
.ladder-table .item td.lay,
.ladder-table .item td.traded {
  text-align:right
}
</style>
"""

DEPTH_TO_WIDTH_MAP = {
    3: '8%',
    4: '16%',
    5: '24%'
}


class Style(Enum):
    DEFAULT = 'default'
    RAW = 'raw'


def calculate_book_percentage(market_book: Dict[str, Any], is_back: bool) -> float:
    implied_probabilities = []
    for runner in market_book['marketDefinition']['runners']:
        if runner['status'] == 'REMOVED':
            continue
        runner_book = None
        best_price = None
        for maybe_runner_book in market_book['runners']:
            if maybe_runner_book['selectionId'] == runner['id']:
                runner_book = maybe_runner_book
                break
        if runner_book:
            if is_back:
                available = runner_book.get('ex', {}).get('availableToBack', [])
            else:
                available = runner_book.get('ex', {}).get('availableToLay', [])
            if available:
                best_price = available[0]['price']

        if best_price:
            implied_probabilities.append(1.0 / best_price)
        else:
            implied_probabilities.append(1.0 if is_back else 0.0)

    return sum(implied_probabilities)


def _create_market_book_button(
        selection_id: int,
        market_book: Union[Dict[str, Any], MarketBook],
        side: str,
        depth: int) -> str:
    if type(market_book) != dict:
        market_book = market_book._data
    html = f'<button class="{side} mv-bet-button ng-isolate-scope {side}{"-selection" if depth == 0 else ""}-button">'
    runner_book = None
    for r in market_book['runners']:
        if r['selectionId'] == selection_id:
            runner_book = r
            break
    if runner_book:
        if side == 'back':
            available = runner_book.get('ex', {}).get('availableToBack', [])
        else:
            available = runner_book.get('ex', {}).get('availableToLay', [])
        if len(available) >= depth + 1:
            html += f'<span class="bet-button-price">{round(available[depth]["price"], 2)}</span>'
            html += f'<span class="bet-button-size">£{round(available[depth]["size"], 2)}</span>'
    html += '</button>'

    return html


def _create_market_book_table(
        market_book: Union[Dict[str, Any], MarketBook],
        depth: int = 3) -> str:
    if type(market_book) != dict:
        market_book = market_book._data
    selection_count = sum(1 for r in market_book['marketDefinition']['runners'] if r['status'] != 'REMOVED')
    html = f"""
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
                        {round(calculate_book_percentage(market_book, True) * 100, 1)}%
                    </th>
                    <th class="rh-select-all-buttons rh-select-back-all-button ng-scope">
                    </th>
                    <th class="rh-select-all-buttons ng-scope">
                    </th>
                    <th class="rh-book-percentage rh-lay-book-percentage ng-scope"
                        style="width: {DEPTH_TO_WIDTH_MAP[depth]}">
                        {round(calculate_book_percentage(market_book, False) * 100, 1)}%
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
        is_non_runner = runner['status'] == 'REMOVED'
        html += ''
        html += f"""
        <tr class="runner-line ng-scope">
            <td class="runner-data-container without-race-card-info">
                <div class="market-graph-container"></div>
                <div>
                    <div class="runner-info">
                        <div class="default name ng-scope">
                            <h3 class="runner-name ng-binding">
                                {runner['name']}{' - Non Runner' if is_non_runner else ''}
                            </h3>
                        </div>
                    </div>
                </div>
            </td>
        """
        for i in range(depth - 1, -1, -1):
            html += '<td class="bet-buttons">'
            html += _create_market_book_button(runner['id'], market_book, 'back', i)
            html += '</td>'
        for i in range(depth):
            html += '<td class="bet-buttons">'
            html += _create_market_book_button(runner['id'], market_book, 'lay', i)
            html += '</td>'
        html += '</tr>'
    html += '</table></div></div>'
    return html


def _create_runner_book_table(runner_book: Union[Dict[str, Any], RunnerBook]) -> str:
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
    all_prices = sorted(set(itertools.chain(price_to_atb.keys(), price_to_atl.keys(), price_to_trd.keys())))
    html = f"""
    <table class="ladder-table" cellspacing="0">
        <thead>
            <tr class="titles">
                <th class="exchange-traded ng-scope" colspan=4>{selection_id}</th>
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
    """
    return html


def _create_market_book_html(
        market_book: Union[Dict[str, Any], MarketBook],
        depth: int = 3) -> str:
    if type(market_book) != dict:
        market_book = market_book._data
    return CSS_STYLE + _create_market_book_table(market_book, depth)


def _create_runner_book_html(runner_book: Union[Dict[str, Any], RunnerBook]) -> str:
    return CSS_STYLE + _create_runner_book_table(runner_book)


def _create_market_book_iframe(
        market_book: Union[Dict[str, Any], MarketBook],
        depth: int = 3) -> str:
    if type(market_book) != dict:
        market_book = market_book._data
    return f"""
        <iframe
            srcdoc="{escape(_create_market_book_html(market_book, depth))}"
            scrolling="no"
            frameBorder="0"
            width=100%
            onload="this.style.height=(this.contentWindow.document.body.scrollHeight+20)+\'px\';">
    """


def _create_runner_book_iframe(runner_book: Union[Dict[str, Any], RunnerBook]) -> str:
    return f"""
        <iframe
            srcdoc="{escape(_create_runner_book_html(runner_book))}"
            scrolling="no"
            frameBorder="0"
            width=100%
            onload="this.style.height=(this.contentWindow.document.body.scrollHeight+20)+\'px\';">
    """


def visualise(
        market_book: Union[Dict[str, Any], MarketBook],
        depth: int = 3,
        style: Union[str, Style] = Style.DEFAULT) -> Union[HTML, Pretty]:
    if (5 < depth) or (depth < 3):
        raise ValueError(f'depth = {depth} is unsupported. Valid values are 3, 4 and 5')
    if type(style) is str:
        style = Style(style)

    if style is Style.DEFAULT:
        return HTML(_create_market_book_iframe(market_book=market_book, depth=depth))
    elif style is Style.RAW:
        return Pretty(pretty(market_book))
    else:
        raise ValueError(f'Unrecognised style: {style}')


visualize = visualise


def _dict_formatter(d: dict) -> str:
    if is_market_book(d):
        return _create_market_book_iframe(d)
    if is_runner_book(d):
        return _create_runner_book_iframe(d)


ip = get_ipython()
if ip:
    ip.display_formatter.formatters['text/html'].for_type(
        MarketBook,
        _create_market_book_iframe
    )
    ip.display_formatter.formatters['text/html'].for_type(
        RunnerBook,
        _create_runner_book_iframe
    )
    ip.display_formatter.formatters['text/html'].for_type(
        dict,
        _dict_formatter
    )
