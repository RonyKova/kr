

try:
    def s(origin):
        def wrapper(v0,v,t):
            d = origin(v0,v,t)
            print ((v0*t)+(d*t**2)/2)
        return wrapper

    @s
    def a(v0,v,t):
        return (v-v0)/t

    a(3,10,3)

except TypeError:
    print('Введены неккоректные значения')
except ZeroDivisionError:
    print('Время не может быть 0')
finally:
    print('Конец программы')






