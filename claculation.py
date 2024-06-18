from baby import speak
from math import operator
import speech_recognition as sr


def cal():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Say what you want to calculate, example: 3 plus 3") 
        def get_operator_fn (op):
            return {
                '+': operator.add, #plus
                '-': operator.sub, #minus
                'x': operator.mul, #multiplied by
                'add': operator.add, #plus
                'substract': operator.sub, #minus
                'times': operator.mul,
                'divided' :operator.__truediv__, #divided
                }[op]
        def eval_binary_expr (op1, oper, op2): # 5
            op1,op2= int(op1), int(op2)
            return get_operator_fn (oper) (op1, op2) 
        speak("your result is") 
        speak(eval_binary_expr(*(my_string.split() )))