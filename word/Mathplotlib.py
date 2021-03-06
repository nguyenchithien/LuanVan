import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
a = [{
    'total_AR_of_central_portfolios': 16.115551876847256,
    'total_AR_of_peripheral_portfolios': 45.679302650246385,
    'total_AR_of_random_portfolios': -87.17744333004927,
    'rd_of_MC_in_selection_horizon': 0.505,
    'rd_of_MC_in_investment_horizon': 0.4950980392156863,
    'rf_of_MC_in_selection_horizon': 0.5092886743507633,
    'rf_of_MC_in_investment_horizon': 0.48238039153205675,
},
    {
    'total_AR_of_central_portfolios': 24.419747836633647,
    'total_AR_of_peripheral_portfolios': 3.5019869653465543,
    'total_AR_of_random_portfolios': 105.21980391089109,
    'rd_of_MC_in_selection_horizon': 0.4975124378109453,
    'rd_of_MC_in_investment_horizon': 0.4876847290640394,
    'rf_of_MC_in_selection_horizon': 0.5104582415017554,
    'rf_of_MC_in_investment_horizon': 0.483433192356265,
},
    {
    'total_AR_of_central_portfolios': -69.21090576499998,
    'total_AR_of_peripheral_portfolios': -96.70799805,
    'total_AR_of_random_portfolios': -107.01964843500001,
    'rd_of_MC_in_selection_horizon': 0.5121951219512195,
    'rd_of_MC_in_investment_horizon': 0.48258706467661694,
    'rf_of_MC_in_selection_horizon': 0.5148022288707713,
    'rf_of_MC_in_investment_horizon': 0.48983256864835567,
},
    {
    'total_AR_of_central_portfolios': 47.80439207999997,
    'total_AR_of_peripheral_portfolios': 114.84149902500002,
    'total_AR_of_random_portfolios': 253.157692875,
    'rd_of_MC_in_selection_horizon': 0.5097087378640777,
    'rd_of_MC_in_investment_horizon': 0.4925373134328358,
    'rf_of_MC_in_selection_horizon': 0.49656641375086297,
    'rf_of_MC_in_investment_horizon': 0.4966683761976731,
},
    {
    'total_AR_of_central_portfolios': -8.442934253731352,
    'total_AR_of_peripheral_portfolios': -13.955223880597014,
    'total_AR_of_random_portfolios': -120.9222393880597,
    'rd_of_MC_in_selection_horizon': 0.5049019607843137,
    'rd_of_MC_in_investment_horizon': 0.504950495049505,
    'rf_of_MC_in_selection_horizon': 0.4943849028184265,
    'rf_of_MC_in_investment_horizon': 0.5107772128350351,
},
    {
    'total_AR_of_central_portfolios': -67.50975347761192,
    'total_AR_of_peripheral_portfolios': 32.19702269651738,
    'total_AR_of_random_portfolios': 215.37915646268658,
    'rd_of_MC_in_selection_horizon': 0.5242718446601942,
    'rd_of_MC_in_investment_horizon': 0.504950495049505,
    'rf_of_MC_in_selection_horizon': 0.5224435525316585,
    'rf_of_MC_in_investment_horizon': 0.5031324193487047,
},
    {
    'total_AR_of_central_portfolios': -183.9564816281407,
    'total_AR_of_peripheral_portfolios': -173.62662924120607,
    'total_AR_of_random_portfolios': -201.70205519597994,
    'rd_of_MC_in_selection_horizon': 0.5194174757281553,
    'rd_of_MC_in_investment_horizon': 0.515,
    'rf_of_MC_in_selection_horizon': 0.5157094495948301,
    'rf_of_MC_in_investment_horizon': 0.5140750095779837,
},
    {
    'total_AR_of_central_portfolios': 10.959595959595958,
    'total_AR_of_peripheral_portfolios': 93.47222222222223,
    'total_AR_of_random_portfolios': 62.4549498888889,
    'rd_of_MC_in_selection_horizon': 0.4951923076923077,
    'rd_of_MC_in_investment_horizon': 0.5226130653266332,
    'rf_of_MC_in_selection_horizon': 0.4927711533717723,
    'rf_of_MC_in_investment_horizon': 0.5155256721532353,
},
    {
    'total_AR_of_central_portfolios': -93.80000000000001,
    'total_AR_of_peripheral_portfolios': -83.883515625,
    'total_AR_of_random_portfolios': 27.597153319999993,
    'rd_of_MC_in_selection_horizon': 0.4854368932038835,
    'rd_of_MC_in_investment_horizon': 0.5223880597014925,
    'rf_of_MC_in_selection_horizon': 0.47604302523375186,
    'rf_of_MC_in_investment_horizon': 0.5183090516582821,
},
    {
    'total_AR_of_central_portfolios': 51.80800684729062,
    'total_AR_of_peripheral_portfolios': -120.84776208374387,
    'total_AR_of_random_portfolios': -322.6899991330049,
    'rd_of_MC_in_selection_horizon': 0.4852941176470588,
    'rd_of_MC_in_investment_horizon': 0.5294117647058824,
    'rf_of_MC_in_selection_horizon': 0.4622405604548203,
    'rf_of_MC_in_investment_horizon': 0.5300185862403506,
},
    {
    'total_AR_of_central_portfolios': -51.68462297058821,
    'total_AR_of_peripheral_portfolios': 30.374521289215696,
    'total_AR_of_random_portfolios': 98.7869131029412,
    'rd_of_MC_in_selection_horizon': 0.4926829268292683,
    'rd_of_MC_in_investment_horizon': 0.526829268292683,
    'rf_of_MC_in_selection_horizon': 0.4781638167596893,
    'rf_of_MC_in_investment_horizon': 0.520824463995732,
},
    {
    'total_AR_of_central_portfolios': -57.23267326732673,
    'total_AR_of_peripheral_portfolios': 0,
    'total_AR_of_random_portfolios': 80.55044283663366,
    'rd_of_MC_in_selection_horizon': 0.49019607843137253,
    'rd_of_MC_in_investment_horizon': 0.5369458128078818,
    'rf_of_MC_in_selection_horizon': 0.4852690106426609,
    'rf_of_MC_in_investment_horizon': 0.5179022442967108,
},

    {
    'total_AR_of_central_portfolios': -22.13941271921182,
    'total_AR_of_peripheral_portfolios': 0,
    'total_AR_of_random_portfolios': -61.129065,
    'rd_of_MC_in_selection_horizon': 0.4801980198019802,
    'rd_of_MC_in_investment_horizon': 0.5637254901960784,
    'rf_of_MC_in_selection_horizon': 0.4856712830723116,
    'rf_of_MC_in_investment_horizon': 0.5506112828968152,
},
    {
    'total_AR_of_central_portfolios': -332.3052210390244,
    'total_AR_of_peripheral_portfolios': 12.317073170731714,
    'total_AR_of_random_portfolios': -57.660003814634145,
    'rd_of_MC_in_selection_horizon': 0.4925373134328358,
    'rd_of_MC_in_investment_horizon': 0.558252427184466,
    'rf_of_MC_in_selection_horizon': 0.4966683761976731,
    'rf_of_MC_in_investment_horizon': 0.5627301403018959,
},
    {
    'total_AR_of_central_portfolios': -3.908903810000025,
    'total_AR_of_peripheral_portfolios': 334.58,
    'total_AR_of_random_portfolios': 529.26599609,
    'rd_of_MC_in_selection_horizon': 0.504950495049505,
    'rd_of_MC_in_investment_horizon': 0.5572139303482587,
    'rf_of_MC_in_selection_horizon': 0.5107772128350351,
    'rf_of_MC_in_investment_horizon': 0.5692804214062773,
},
    {
    'total_AR_of_central_portfolios': 65.360385745,
    'total_AR_of_peripheral_portfolios': -126.56250976500002,
    'total_AR_of_random_portfolios': -108.35050292999999,
    'rd_of_MC_in_selection_horizon': 0.5024630541871922,
    'rd_of_MC_in_investment_horizon': 0.5621890547263682,
    'rf_of_MC_in_selection_horizon': 0.5021000255208866,
    'rf_of_MC_in_investment_horizon': 0.5844798124560739,
},
    {
    'total_AR_of_central_portfolios': -112.85635390640395,
    'total_AR_of_peripheral_portfolios': -119.2433612955665,
    'total_AR_of_random_portfolios': -32.09556842364533,
    'rd_of_MC_in_selection_horizon': 0.515,
    'rd_of_MC_in_investment_horizon': 0.5735294117647058,
    'rf_of_MC_in_selection_horizon': 0.5140750095779837,
    'rf_of_MC_in_investment_horizon': 0.60387261282921,
},
    {
    'total_AR_of_central_portfolios': 873.0387417598039,
    'total_AR_of_peripheral_portfolios': -77.84313725490198,
    'total_AR_of_random_portfolios': 478.3843156421568,
    'rd_of_MC_in_selection_horizon': 0.525,
    'rd_of_MC_in_investment_horizon': 0.5707317073170731,
    'rf_of_MC_in_selection_horizon': 0.5160326846039247,
    'rf_of_MC_in_investment_horizon': 0.5783593416390611,
},
    {
    'total_AR_of_central_portfolios': 30.111337743842387,
    'total_AR_of_peripheral_portfolios': 195.8950796650246,
    'total_AR_of_random_portfolios': 219.22438327586207,
    'rd_of_MC_in_selection_horizon': 0.5247524752475248,
    'rd_of_MC_in_investment_horizon': 0.5833333333333334,
    'rf_of_MC_in_selection_horizon': 0.5203904561151363,
    'rf_of_MC_in_investment_horizon': 0.6128878033100472,
},
    {
    'total_AR_of_central_portfolios': 40.82288501020405,
    'total_AR_of_peripheral_portfolios': 61.599988040816314,
    'total_AR_of_random_portfolios': -42.815100846938776,
    'rd_of_MC_in_selection_horizon': 0.526829268292683,
    'rd_of_MC_in_investment_horizon': 0.5685279187817259,
    'rf_of_MC_in_selection_horizon': 0.5290848774088479,
    'rf_of_MC_in_investment_horizon': 0.6169296719020544,
},
    {
    'total_AR_of_central_portfolios': -5.837357954545458,
    'total_AR_of_peripheral_portfolios': -119.7919231363636,
    'total_AR_of_random_portfolios': -53.815101702020186,
    'rd_of_MC_in_selection_horizon': 0.526829268292683,
    'rd_of_MC_in_investment_horizon': 0.5628140703517588,
    'rf_of_MC_in_selection_horizon': 0.520824463995732,
    'rf_of_MC_in_investment_horizon': 0.618339788172022,
},
    {
    'total_AR_of_central_portfolios': 0.38392156281406686,
    'total_AR_of_peripheral_portfolios': -6.934673366834174,
    'total_AR_of_random_portfolios': 86.24839038693467,
    'rd_of_MC_in_selection_horizon': 0.5343137254901961,
    'rd_of_MC_in_investment_horizon': 0.555,
    'rf_of_MC_in_selection_horizon': 0.5167677925977852,
    'rf_of_MC_in_investment_horizon': 0.5899912637251167,
},

    {
    'total_AR_of_central_portfolios': -24.288873163265308,
    'total_AR_of_peripheral_portfolios': -249.515306122449,
    'total_AR_of_random_portfolios': -100.42367366836733,
    'rd_of_MC_in_selection_horizon': 0.5658536585365853,
    'rd_of_MC_in_investment_horizon': 0.5431472081218274,
    'rf_of_MC_in_selection_horizon': 0.5533607034381917,
    'rf_of_MC_in_investment_horizon': 0.5807827047455791,
},
    {
    'total_AR_of_central_portfolios': -60.258581909090914,
    'total_AR_of_peripheral_portfolios': -64.36868686868686,
    'total_AR_of_random_portfolios': 24.53212298989899,
    'rd_of_MC_in_selection_horizon': 0.5594059405940595,
    'rd_of_MC_in_investment_horizon': 0.5477386934673367,
    'rf_of_MC_in_selection_horizon': 0.5726859519114749,
    'rf_of_MC_in_investment_horizon': 0.5371127509422876,
},

    {
    'total_AR_of_central_portfolios': -10.312825517948724,
    'total_AR_of_peripheral_portfolios': -44.96958884102564,
    'total_AR_of_random_portfolios': 77.03471805128203,
    'rd_of_MC_in_selection_horizon': 0.558252427184466,
    'rd_of_MC_in_investment_horizon': 0.5561224489795918,
    'rf_of_MC_in_selection_horizon': 0.5627301403018959,
    'rf_of_MC_in_investment_horizon': 0.551240722279712,
}]
# 'day_t' = []
# for o in a:
#     string_day = o[''day_t'']
#     dtime = datetime.date(int(string_day[:4]), int(
#         string_day[5:7]), int(string_day[8:10]))
#     'day_t'.append(dtime)
# '''rf_of_MC_in_selection_horizon''' = []
# for o in a:
#     string_day = o[''''rf_of_MC_in_investment_horizon'''']
#     '''rf_of_MC_in_selection_horizon'''.append(string_day)
# print('''rf_of_MC_in_selection_horizon''')
sum = 0
for o in a:
    sum += o['total_AR_of_peripheral_portfolios']

print(sum)
# plt.plot_date('day_t', '''rf_of_MC_in_selection_horizon''', 'ro')
# plt.show()
