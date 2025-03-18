import json

# define data
# data includes:
# description of the case, context (only for historical events),
# solution options, which include:
# description of the solutions, variables that will be adjusted and the modifiers.

# lic_events.py has ALL events now #

# low income level events
lic_events_dict = {"lic_events": [# event list
    {# one event ## The Great Famine of Ireland (1845-1852)
        "event_description": "A potato crop disease has been going around, "
                       "causing a large scale of crop failure. "
                       "The majority of the population depends on this plant as both their source of income and food.",
        "context": " The Great Famine of Ireland (1845-1852): A potato crop failure, worsened by British policies, "
                   "led to mass starvation and the death of about a million people. "
                   "The famine caused widespread emigration, "
                   "drastically reducing Ireland’s population and "
                   "leaving a lasting impact on its economy "
                   "and its relationship with Britain.",
        "solution_options": [{
            "solution_1": "Subsidise Food Imports: Import food to stabilize prices and supply.",
            "food_supply": +0.5,
            "price_level": -0.2,
            "national_debt": +0.4,
            "public_spending": +0.3,
            "happiness_index": +0.2
        }, {
            "solution_2": "Encourage Alternative Crops: Promote crops other than potatoes to reduce dependence.",
            "food_supply": +0.3,
            "resource_gathering_efficiency": +0.4,
            "price_level": -0.1,
            "GDP": +0.2,
            "happiness_index": +0.1
        }, {
            "solution_3": "Send International Aid: Accept British relief and international food aid.",
            "food_supply": +0.4,
            "national_debt": +0.2,
            "public_spending": +0.2,
            "GDP": +0.1
        }]
    },
{# one event ## The Debt Crisis of the 1980s
        "event_description": "Debt can be damaging to the economy when borrowing excessively from international lenders, "
                             "especially when global interest rates are rising. "
                             "What would you do to reduce the pressure on finance?",
        "context": "The Debt Crisis of the 1980s: Many developing countries, especially in Latin America, "
                       "struggled with massive debt due to excessive borrowing "
                       "and rising interest rates. This led to economic instability, "
                       "hyperinflation, and social unrest, requiring international intervention "
                       "to restructure debt and impose austerity measures.",
        "solution_options": [{
            "solution_1": "Renegotiate Debt: Work with international lenders to restructure the debt.",
            "national_debt": -0.3,
            "GDP": +0.2,
            "tax_revenue": +0.2,
            "public_spending": -0.1
        }, {
            "solution_2": "Introduce Austerity Measures: Cut government spending to reduce debt.",
            "national_debt": -0.5,
            "public_spending": -0.5,
            "unemployment_rate": +0.3,
            "GDP": -0.3
        }, {
            "solution_3": "Seek International Bailouts: Receive aid and loans from the IMF and World Bank.",
            "national_debt": -0.2,
            "GDP": -0.1,
            "public_spending": -0.2,
            "tax_revenue": +0.1
        }]
    },
{# one event ## The Bangladesh Garment Factory Collapse (2013)
        "event_description": "A large factory has collapsed. Most of the workers inside the building were injured severely, "
                             "many of them did not survive. Majority of the labour force and firms in the manufacturing sector is extremely concerned.",
        "context": "The Bangladesh Garment Factory Collapse (2013): The collapse of Rana Plaza, a building housing garment factories, "
                   "killed over 1,100 workers and exposed unsafe labor conditions. "
                   "The disaster highlighted the dangers of global supply chains "
                   "prioritizing low costs over worker safety and ethical practices.",
        "solution_options": [{
            "solution_1": "Improve Worker Safety Standards: Introduce regulations to ensure safer working conditions.",
            "business_efficiency": -0.1,
            "public_spending": +0.2,
            "happiness_index": +0.3
        }, {
        "solution_2": "Increase Inspection: Set up regular government inspections for factory compliance.",
            "business_efficiency": -0.2,
            "public_spending": +0.3,
            "GDP": -0.1
        }, {
        "solution_3": "Raise Wages and Improve Conditions: Pressure manufacturers to improve wages and conditions Raise Wages and Improve Conditions: Pressure manufacturers to improve wages and conditions.",
            "business_efficiency": -0.3,
            "happiness_index": +0.5,
            "price_level": +0.2
        }]
    },
{# one event
        #"event_name": "Food Shortages and Rising Prices",
        "event_description": "A major river just flooded yesterday, destroying many crops that were about to be harvested. "
                       "There could be food shortages and rising prices for food in the coming months.",
        "context": None,
        "solution_options": [{
            "solution_1": "Subsidize Food Imports: Reduce costs of essential food items.",
            "food_supply": +0.5,
            "price_level": -0.3,
            "national_debt": +0.4
        }, {
            "solution_2": "Invest in Agricultural Subsidies: Increase local food production through support to farmers.",
            "resource_gathering_efficiency": +0.4,
            "GDP": +0.3,
            "price_level": -0.1
        }, {
            "solution_3": "Enforce Price Controls: Set maximum price limits for staple foods to prevent exploitation.",
            "price_level": -0.5,
            "supply": -0.3,
            "happiness_index": +0.2
        }]
    },
{# one event
        #"event_name": "High Unemployment in Rural Areas",
        "event_description": "Young people who grew up in rural area have very little access to career opportunities, "
                       "resulting in high unemployment in those areas.",
        "context": None,
        "solution_options": [{
            "solution_1": "Build Rural Infrastructure: Invest in roads, schools, and utilities to make rural life more sustainable.",
            "unemployment_rate": -0.4,
            "GDP": +0.3,
            "public_spending": +0.4,
            "resource_gathering_efficiency": +0.2
        }, {
            "solution_2": "Start Public Works Projects: Create jobs through large-scale infrastructure development.",
            "unemployment_rate": -0.5,
            "GDP": +0.2,
            "national_debt": +0.3,
            "public_spending": +0.5
        }, {
            "solution_3": "Promote Microfinance Programs: Encourage entrepreneurship through small loans for rural entrepreneurs.",
            "unemployment_rate": -0.3,
            "business_efficiency": +0.3,
            "GDP": +0.2,
            "tax_revenue": +0.2
        }]
    },
{# one event
        #"event_name": "Healthcare Crisis",
        "event_description": "An unknown infectious disease is rapidly spreading in the country. "
                       "The country currently does not have the knowledge and resources to treat patients who are suffering from it.",
        "context": None,
        "solution_options": [{
            "solution_1": "Increase Healthcare Spending: Allocate more budget to healthcare to improve services and facilities.",
            "life_expectancy": +0.5,
            "happiness_index": +0.4,
            "public_spending": +0.5,
            "national_debt": +0.2
        }, {
            "solution_2": "Partner with NGOs for Aid: Collaborate with international aid organizations to address immediate needs.",
            "life_expectancy": +0.3,
            "happiness_index": +0.3,
            "public_spending": +0.2
        }, {
            "solution_3": "Focus on Preventive Measures: Promote sanitation, vaccination programs, and health education to prevent disease outbreaks.",
            "life_expectancy": +0.4,
            "happiness_index": +0.3,
            "public_spending": +0.3,
            "GDP": +0.2
        }]
    }
]
               }

# medium income level events
mic_events_dict = {"mic_events": [# event list
    {# one event
        "event_description": "A region experiencing rapid economic growth suddenly faces a financial collapse as investor confidence plummets.",
        "context": "The Asian Financial Crisis (1997): "
                   "A sudden loss of investor confidence triggers a financial meltdown across several Asian economies. "
                   "Currency values plummet, stock markets crash, and foreign capital rapidly exits, leading to deep recessions. "
                   "Governments scramble to stabilize their economies, turning to international institutions for emergency assistance.",
        "solution_options": [{
            "solution_1": "Raise Interest Rates: Increase rates to stabilize currency and reduce inflation.",
            "inflation_rate": -0.4,
            "GDP": -0.3,
            "unemployment_rate": +0.2
        }, {
            "solution_2": "Offer Government Bailouts: Provide emergency loans to struggling businesses.",
            "national_debt": +0.3,
            "GDP": +0.2,
            "tax_revenue": -0.1
        }, {
            "solution_3": "Seek International Aid: Accept financial support from the IMF",
            "national_debt": +0.2,
            "GDP": -0.1,
            "public_spending": -0.1
        }]
    },
{# one event
        "event_description": "The country facing years of heavy borrowing and currency instability plunges into a severe economic crisis, "
                             "leading to widespread public outrage and protests erupt",
        "context": "The Argentine Economic Crisis (1998-2002): "
                   "Years of heavy borrowing and currency instability push Argentina into a severe economic crisis. "
                   "Inflation skyrockets, unemployment soars, and bank runs lead to financial chaos. "
                   "Drastic government measures fail to restore confidence, sparking mass protests and political upheaval.",
        "solution_options": [{
            "solution_1": "Devalue the Currency: Allow the currency to lose value to boost exports.",
            "exports": +0.5,
            "inflation_rate": +0.6,
            "demand": -0.3
        }, {
            "solution_2": "Increase Taxes: Raise taxes on businesses to generate revenue.",
            "tax_revenue": +0.3,
            "GDP": -0.2,
            "happiness_index": -0.3
        }, {
            "solution_3": "Dollarise the Economy: Peg the peso to the U.S. dollar.",
            "inflation_rate": -0.6,
            "GDP": +0.4,
            "price_level": -0.2
        }]
    },
{# one event
        "event_description": "A nation burdened by massive debt struggles to meet its financial obligations. "
                             "As public frustration grows over spending cuts and economic hardship, leaders must find a path to recovery while maintaining social stability.",
        "context": "The Greek Debt Crisis (2009): "
                   "Greece’s massive debt burden and economic mismanagement push the country toward financial collapse. "
                   "Investors demand higher interest rates, making it harder to repay loans, forcing Greece to seek international bailouts. "
                   "Austerity measures follow, leading to widespread protests, economic hardship, and political instability.",
        "solution_options": [{
            "solution_1": "Implement Austerity: Cut government spending to reduce the deficit.",
            "national_debt": -0.5,
            "public_spending": -0.5,
            "unemployment_rate": +0.4,
            "GDP": -0.3
        }, {
            "solution_2": "Increase Taxes: Raise taxes on the wealthy and corporations.",
            "tax_revenue": +0.3,
            "GDP": -0.3,
            "business_efficiency": -0.2
        }, {
            "solution_3": "Negotiate EU Bailouts: Seek financial assistance from the EU and the ECB ",
            "national_debt": -0.2,
            "GDP": -0.1,
            "public_spending": -0.1,
            "tax_revenue": +0.1
        }]
    },
{# one event
        "event_description": "Inflation and rising cost of living has been stressing people. "
                             "Many are finding it difficult to afford goods and services that are necessary for daily life.",
        "context": None,
        "solution_options": [{
            "solution_1": "Raise Interest Rates: Increase borrowing costs to slow inflation and stabilize currency.",
            "inflation_rate": -0.4,
            "GDP": -0.2,
            "unemployment_rate": +0.2
        }, {
            "solution_2": "Subsidise Essential Goods: Provide government subsidies to reduce the impact of rising prices on households.",
            "price_level": -0.3,
            "national_debt": +0.3,
            "tax_revenue": -0.2
        }, {
            "solution_3": "Implement Wage Controls: Limit wage increases to match productivity and help contain inflation.",
            "business_efficiency": -0.2,
            "inflation_rate": -0.1,
            "happiness_index": -0.3
        }]
    },
{# one event
        "event_description": "The growth of public debt is accelerating. Pressure on public finance is very high.",
        "context": None,
        "solution_options": [{
            "solution_1": "Negotiate Debt Relief: Renegotiate terms with creditors to lower the debt burden.",
            "national_debt": -0.4,
            "GDP": +0.3,
            "public_spending": -0.2
        }, {
            "solution_2": "Raise Taxes: Increase taxes on corporations and the wealthy to improve fiscal balance.",
            "tax_revenue": +0.3,
            "GDP": -0.2,
            "business_efficiency": -0.1
        }, {
            "solution_3": "Cut Public Spending: Reduce government expenditures, especially in non-essential sectors.",
            "national_debt": -0.3,
            "public_spending": -0.5,
            "happiness_index": -0.2
        }]
    },
{# one event
        "event_description": "Income inequality is getting worse, and people are angry in the country, that they are prepared to riot.",
        "context": None,
        "solution_options": [{
            "solution_1": "Progressive Taxation: Implement higher taxes on the wealthy to redistribute income.",
            "tax_revenue": +0.4,
            "happiness_index": +0.3,
            "business_efficiency": -0.2
        }, {
            "solution_2": "Expand Social Welfare Programs: Provide more social safety nets for lower-income citizens.",
            "happiness_index": +0.4,
            "public_spending": +0.3,
            "GDP": +0.2
        }, {
            "solution_3": "Promote Economic Growth through Business Incentives: Offer tax breaks and support for businesses to create more jobs.",
            "business_efficiency": +0.4,
            "GDP": +0.3,
            "tax_revenue": +0.2
        }]
    }
]
}

# high income level events
hic_events_dict = {"hic_events": [# event list
{# one event
        "event_description": "A sudden financial collapse triggers a severe economic downturn, causing businesses to fail, banks to close, and unemployment to skyrocket. With industries struggling and millions facing poverty, consumer confidence plummets, deepening the crisis.",
        "context": "The Great Depression (1929): A massive stock market crash triggers a global economic collapse, "
                   "leading to widespread bank failures, business closures, and soaring unemployment. "
                   "Industrial production plummets, and millions of people struggle with poverty and homelessness. "
                   "Governments attempt various recovery measures, but the crisis lingers for years, reshaping economic policies worldwide.",
        "solution_options": [{
            "solution_1": "Increase Public Works: Invest in infrastructure projects to create jobs.",
            "unemployment_rate": -0.6,
            "GDP": +0.4,
            "national_debt": +0.3
        }, {
            "solution_2": "Lower Interest Rates: Reduce borrowing costs to stimulate investment and spending.",
            "GDP": +0.3,
            "inflation_rate": +0.1,
            "demand": +0.4
        }, {
            "solution_3": "New Deal Programs: Implement government relief programs ",
            "unemployment_rate": -0.7,
            "national_debt": +0.5,
            "GDP": +0.4
        }]
    },
{# one event
        "event_description": "",
        "context": "The Global Financial Crisis (2007-2008): A housing market collapse in the U.S. sparks a global financial meltdown, "
                   "as major banks and institutions face insolvency. Stock markets crash, unemployment rises, and economies worldwide enter deep recessions. "
                   "Governments and central banks intervene with massive bailouts and stimulus programs to prevent total collapse.",
        "solution_options": [{
            "solution_1": "Bail Out Banks: Use taxpayer money to support failing banks and prevent further collapse.",
            "GDP": +0.3,
            "national_debt": +0.5,
            "tax_revenue": -0.2
        }, {
            "solution_2": "Increase Government Spending: Stimulate the economy through fiscal policies and infrastructure investment.",
            "public_spending": +0.5,
            "GDP": +0.4,
            "national_debt": +0.3
        }, {
            "solution_3": "Quantitative Easing: Central banks (such as the Federal Reserve) flood the market with money to stabilize the economy.",
            "inflation_rate": +0.2,
            "GDP": +0.3,
            "business_efficiency": +0.4
        }]
    },
{# one event
        "event_description": "",
        "context": "The 1973 Oil Crisis: A sudden oil embargo by major producers causes global oil prices to skyrocket, "
                             "leading to fuel shortages and economic turmoil. Inflation surges, industries struggle, and many economies fall into recession. "
                             "Governments implement energy-saving measures and seek alternative energy sources to reduce dependence on foreign oil.",
        "solution_options": [{
            "solution_1": "Ration Fuel and Enforce Conservation: Implement restrictions on fuel consumption to manage shortages.",
            "demand": -0.3,
            "GDP": -0.4,
            "inflation_rate": +0.3
        }, {
            "solution_2": "Invest in Alternative Energy: Expand research and infrastructure for renewable energy sources.",
            "R&D_efficiency": +0.5,
            "GDP": +0.2,
            "national_debt": +0.3
        }, {
            "solution_3": "Government Imposes Price Controls & Diplomacy: Limit oil prices domestically and engage in diplomatic efforts to stabilize supply.",
            "inflation_rate": -0.3,
            "GDP": -0.2,
            "supply": +0.2
        }]
    },
{# one event
        "event_description": "A country experiences slow economic growth for an extended period, with low productivity and weak investment. "
                             "Wages stagnate, unemployment remains high, and businesses struggle to expand.",
        "context": None,
        "solution_options": [{
            "solution_1": "Invest in Technological Innovation: Fund R&D and innovation to improve productivity and create new industries.",
            "GDP": +0.4,
            "R&D_efficiency": +0.5,
            "business_efficiency": +0.3
        }, {
            "solution_2": "Stimulate Consumer Spending through Tax Cuts: Reduce taxes to increase disposable income and consumption.",
            "GDP": +0.3,
            "tax_revenue": -0.3,
            "price_level": +0.2
        }, {
            "solution_3": "Open New Trade Markets: Seek new international trade agreements to diversify exports and investments.",
            "GDP": +0.4,
            "supply": +0.3,
            "business_efficiency": +0.2
        }]
    },
{# one event
        "event_description": "Advancements in technology and automation replace many traditional jobs, leaving a large portion of the workforce unemployed. "
                             "Many struggle to find new opportunities, leading to economic inequality.",
        "context": None,
        "solution_options": [{
            "solution_1": "Implement Job Retraining Programs: Offer government-funded programs to retrain workers for new industries.",
            "R&D_efficiency": +0.3,
            "unemployment_rate": -0.4,
            "GDP": +0.2
        }, {
            "solution_2": "Provide Universal Basic Income (UBI): Offer citizens a fixed monthly income to support economic stability.",
            "happiness_index": +0.6,
            "national_debt": +0.4,
            "tax_revenue": -0.3
        }, {
            "solution_3": "Offer Tax Incentives for Labor-Intensive Industries: Encourage businesses that create jobs in manufacturing and services.",
            "happiness_index": +0.6,
            "national_debt": +0.4,
            "tax_revenue": -0.3
        }]
    },
{# one event
        "event_description": "Widespread industrial activity and weak regulations lead to severe pollution, harming public health and ecosystems. "
                             "Air, water, and soil contamination drive climate change and resource shortages, threatening economic stability.",
        "context": None,
        "solution_options": [{
            "solution_1": "Implement Green Taxes: Introduce taxes on carbon emissions and other polluting activities to encourage sustainable practices.",
            "tax_revenue": +0.5,
            "business_efficiency": -0.3,
            "pollution": -0.4
        }, {
            "solution_2": "Invest in Renewable Energy: Increase funding for solar, wind, and other renewable energy sources to transition away from fossil fuels.",
            "R&D_efficiency": +0.5,
            "GDP": +0.3,
            "national_debt": +0.4
        }, {
            "solution_3": "Regulate Pollution: Strengthen environmental laws and regulations to reduce industrial emissions and promote cleaner practices.",
            "pollution": -0.5,
            "business_efficiency": -0.2,
            "GDP": -0.2
        }]
    }
]
               }

# write to a json file
with open("all_events.json", "w") as file:
    json.dump(lic_events_dict, file, indent=4)
with open("mic_events.json", "w") as file:
    json.dump(mic_events_dict, file, indent=4)
with open("hic_events.json", "w") as file:
    json.dump(hic_events_dict, file, indent=4)