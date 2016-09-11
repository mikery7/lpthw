name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
lb_to_kilo = weight * 0.45359237
in_to_centi = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall, which is %d centimeters." % (height, round(in_to_centi))
print "He's %d pounds heavy, which is %d kilos." % (weight, round(lb_to_kilo))
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
