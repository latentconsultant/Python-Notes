#Inheritence

'''Demonstrate class inheritence '''
class Base_Model():
    ''' Represent the base model of the car '''
    trim = 'normal'
    engine_liters = 1.5

    def engine_sound(self):
        return 'putt, putt'

    def horn_sound(self):
        return 'beep, beep'

    def __str__(self):
        return 'Base Model'

coop = Base_Model()
print('%s has %s trim level.' % (coop, coop.trim))
print('%s has a %s liter engine.' % (coop, coop.engine_liters))
print('%s engine sounds like %s.' % (coop, coop.engine_sound()))
print('%s horn sounds like %s.' % (coop, coop.horn_sound()))

class Sport_Model(Base_Model):
    engine_liters = 2.0

    def engine_sound(self):
        return 'VROOM, VROOM'

    def horn_sound(self):
        return 'BEEP, BEEP'

    def __str__(self):
        return 'Sport Model'

coop_sport = Sport_Model()
print('%s has %s trim level.' % (coop_sport, coop_sport.trim))
print('%s has a %s liter engine.' % (coop_sport, coop_sport.engine_liters))
print('%s engine sounds like %s.' % (coop_sport, coop_sport.engine_sound()))
print('%s horn sounds like %s.' % (coop_sport, coop_sport.horn_sound()))

class Luxury_Model(Base_Model):
    trim = 'luxury'

    def engine_sound(self):
        return 'vroom, vroom'

    def horn_sound(self):
        return 'honk, honk'

    def __str__(self):
        return 'Luxury Model'

class Luxury_Sport_Model(Luxury_Model, Sport_Model):
    def __str__(self):
        return 'Luxury Sport Model'

coop_luxury_sport = Luxury_Sport_Model()
print('%s has %s trim level.' % (coop_luxury_sport, coop_luxury_sport.trim))
print('%s has a %s liter engine.' % (coop_luxury_sport, coop_luxury_sport.engine_liters))
print('%s engine sounds like %s.' % (coop_luxury_sport, coop_luxury_sport.engine_sound()))
print('%s horn sounds like %s.' % (coop_luxury_sport, coop_luxury_sport.horn_sound()))

class Sport_Luxury_Model(Sport_Model, Luxury_Model):
    def __str__(self):
        return 'Sport Luxury Model'

coop_sport_luxury = Sport_Luxury_Model()
print('%s has %s trim level.' % (coop_sport_luxury, coop_sport_luxury.trim))
print('%s has a %s liter engine.' % (coop_sport_luxury, coop_sport_luxury.engine_liters))
print('%s engine sounds like %s.' % (coop_sport_luxury, coop_sport_luxury.engine_sound()))
print('%s horn sounds like %s.' % (coop_sport_luxury, coop_sport_luxury.horn_sound()))

coop_custom = Sport_Luxury_Model()
print('%s has %s trim level.' % (coop_custom, coop_custom.trim))
coop_custom.trim = 'custom'
print('%s now has %s trim level.' % (coop_custom, coop_custom.trim))
print('The class %s still has %s trim level.' % (Sport_Luxury_Model, Sport_Luxury_Model.trim))
coop_custom.brakes = 'racing'
Base_Model.brakes = 'standard'
print('%s has %s brakes.' % (coop_custom, coop_custom.brakes))
print('%s has %s brakes.' % (Sport_Luxury_Model, Sport_Luxury_Model.brakes))





    
