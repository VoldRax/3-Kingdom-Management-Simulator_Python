This is exactly the level of detail we need. I'll also make one important architectural change:

Models should own their own data and simple behavior.
Services should coordinate multiple models or perform application logic.

This is the architecture we'll stick to for the whole project.

📁 models/

Models represent things that exist in the game.

Kingdom

The Kingdom is just the root object.

It owns everything.

class Kingdom
Attributes
name
turn

economy
population
army
resources

buildings
Methods
next_turn()

get_summary()

to_dict()

from_dict()
Purpose
Own every subsystem
Serialize itself
Advance turn counter

NOT

Collect taxes
Train army
Save game
Print reports

Economy
class Economy
Attributes
gold
tax_rate
trade_income
maintenance_cost
Methods
add_gold(amount)

remove_gold(amount)

can_afford(amount)

change_tax_rate(rate)

calculate_total_income()

calculate_total_expenses()

Notice

Economy knows about money only.

Population
class Population
Attributes
total

workers

farmers

merchants

soldiers

scholars

happiness

health
Methods
increase(amount)

decrease(amount)

change_happiness(amount)

change_health(amount)

assign_workers(job, amount)

No taxes here.

No food.

Only people.

Resources
class Resources
Attributes
food

wood

stone

iron

coal
Methods
add(resource, amount)

remove(resource, amount)

has(resource, amount)

consume_food(amount)
Army
class Army
Attributes
infantry

archers

cavalry

morale
Methods
recruit(unit, amount)

dismiss(unit, amount)

change_morale(amount)

calculate_power()
Building

This is where beginners usually make mistakes.

Don't create

farm.py

mine.py

market.py

castle.py

Yet.

Instead

class Building

Attributes

name

level

cost

maintenance

workers_required

Methods

upgrade()

downgrade()

maintenance_cost()

bonus()

Then create

class Farm(Building)

Methods

produce_food()
class Mine(Building)

Methods

produce_iron()

produce_coal()
class Market(Building)

Methods

generate_trade_income()
class Barracks(Building)

Methods

train_units()
class Hospital(Building)

Methods

heal_population()
class School(Building)

Methods

educate_population()

So every building only knows how itself works.

BuildingManager

This owns every building.

class BuildingManager

Attributes

buildings

Methods

construct()

destroy()

upgrade()

find()

count()

all()
📁 services/

These coordinate models.

EconomyService

Responsibilities

Taxes
Trade
Expenses

Methods

collect_taxes(kingdom)

calculate_trade_income(kingdom)
trade_income = (merchants × 2 + population × 0.1 + market_bonus) × happiness_modifier

pay_maintenance(kingdom)

buy_food(kingdom, amount)

sell_resources(kingdom)

Notice

EconomyService modifies

Economy

Resources

Population

Sometimes more than one.

That's why it's a service.

PopulationService

Methods

grow_population(kingdom)

calculate_births(kingdom)

calculate_deaths(kingdom)

update_happiness(kingdom)

starvation_check(kingdom)

Touches

Population

Resources
ArmyService

Methods

train_soldiers(kingdom)

feed_army(kingdom)

battle(attacker, defender)

calculate_losses()

pay_wages()

Touches

Army

Economy

Resources
BuildingService

Methods

construct_building(kingdom)

upgrade_building(kingdom)

repair_building(kingdom)

demolish_building(kingdom)

collect_building_production(kingdom)

Touches

Buildings

Resources

Economy
EventService

Methods

trigger_random_event()

apply_event()

load_events()

Touches

Everything.

SaveService

Methods

save()

load()

autosave()

Touches

Nothing.

Only files.

ReportService

Methods

kingdom_report()

economy_report()

army_report()

population_report()

resource_report()

Reads data.

Never modifies.

MenuService (optional)

Methods

show_main_menu()

show_reports()

show_buildings()

show_army()
What Happens When User Collects Taxes?
Player

↓

Menu

↓

EconomyService.collect_taxes()

↓

Population.total

↓

Economy.add_gold()

↓

ReportService.kingdom_report()

Notice

The service uses the models.

The models don't call each other randomly.

Golden Rule
Question	Goes In
Does it store state?	Model
Does it change one model?	Usually a model method
Does it coordinate multiple models?	Service
Does it read/write files?	SaveService
Does it print something?	ReportService/UI
Does it handle user input?	Menu/UI
One change I would make

I would not create EconomyService, ArmyService, PopulationService, etc. immediately.

Instead, for V1 I'd create just these:

models/
├── kingdom.py
├── economy.py
├── population.py
├── army.py
├── resources.py
├── building.py
└── building_manager.py

services/
├── game_service.py
├── save_service.py
├── report_service.py
└── event_service.py