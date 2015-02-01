#imports
import webiopi

# Libreria GPIO
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Definicion constantes                           #
# -------------------------------------------------- #

# GPIOs motor izquierdo
L1=10  # H-Bridge 1
L2=9 # H-Bridge 2
Le=23 # PWM left

# GPIOs motor derecho
R1=17 # H-Bridge 3
R2=21 # H-Bridge 4
Re=22 #Enable PWM Right

# -------------------------------------------------- #
# Funciones motor izquierdo                          #
# -------------------------------------------------- #

def left_stop():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)
    

def left_forward():
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(L2, GPIO.LOW)
    
def left_backward():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)

# -------------------------------------------------- #
# Funciones motor derecho                            #
# -------------------------------------------------- #

def right_stop():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

def right_forward():
    GPIO.output(R1, GPIO.HIGH)
    GPIO.output(R2, GPIO.LOW)

def right_backward():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)


#--------------------------------#
#Velocidades                     #
#--------------------------------#

def vel_left(ve):
    GPIO.pulseRatio(Le, ve)

def vel_right(vel):
    GPIO.pulseRatio(Re, vel)


# -------------------------------------------------- #
# Definicion macros                               #
# -------------------------------------------------- #

@webiopi.macro
def go_forward():
    left_forward()
    right_forward()
    vel_left(1)
    vel_right(1)

@webiopi.macro
def go_backward():
    left_backward()
    right_backward()
    vel_left(0.5)
    vel_right(0.5)

@webiopi.macro
def turn_left():
    right_forward()
    left_backward()
    vel_left(0.2)
    vel_right(0.2)

@webiopi.macro
def turn_right():
    right_backward()
    left_forward()
    vel_left(0.2)
    vel_right(0.2)

@webiopi.macro    
def stop():
    left_stop()
    right_stop()
    vel_left(0)
    vel_right(0)
    
# -------------------------------------------------- #
# Iniciacializacion                                  #
# -------------------------------------------------- #

def setup():
# Instalacion GPIOs
    GPIO.setFunction(L1, GPIO.OUT)
    GPIO.setFunction(L2, GPIO.OUT)

    GPIO.setFunction(R1, GPIO.OUT)
    GPIO.setFunction(R2, GPIO.OUT)
	
    GPIO.setFunction(Re, GPIO.PWM)
    GPIO.setFunction(Le, GPIO.PWM)

def destroy():
    # Resetea las funciones GPIO
    GPIO.setFunction(L1, GPIO.IN)
    GPIO.setFunction(L2, GPIO.IN)

    GPIO.setFunction(R1, GPIO.IN)
    GPIO.setFunction(R2, GPIO.IN)

    GPIO.setFunction(Le, GPIO.IN)
    GPIO.setFunction(Re, GPIO.IN)
