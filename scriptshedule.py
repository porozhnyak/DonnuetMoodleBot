import datetime
import time
import json


def article():
    id = int(str(datetime.datetime.today().isoweekday())+str(datetime.datetime.today().strftime('%H%M')))
    print(id)


#with open("data_lesson.json", "w") as file:
    #json.dump(shedule, file, indent=4, ensure_ascii=False)



class My_Times:

    def monday():

        def first():
            shedule = {}

            lesson1 = int(input("Введите первую пару по верхней неделе: "))
            lesson2 = int(input("Введите первую пару по нижней неделе: "))

            
            first = list(range(10830, 10859, 5)) + list(range(10900, 10959, 5))
            for i in first:
                if lesson1 == 0:
                    lesson1 = None
                if lesson2 == 0:
                    lesson2 = None

                shedule[i] = {
                    "lesson1": lesson1,
                    "lesson2": lesson2
                }
            return shedule

        def second():
            shedule = {}

            lesson1 = int(input("Введите вторую пару по верхней неделе: "))
            lesson2 = int(input("Введите вторую пару по нижней неделе: "))

            
            second = list(range(11015, 11059, 5)) + list(range(11100, 11145, 5))
            for i in second:
                if lesson1 == 0:
                    lesson1 = None
                if lesson2 == 0:
                    lesson2 = None

                shedule[i] = {
                    "lesson1": lesson1,
                    "lesson2": lesson2
                }
            return shedule

        def third():
            shedule = {}

            lesson1 = int(input("Введите третью пару по верхней неделе: "))
            lesson2 = int(input("Введите третью пару по нижней неделе: "))

            
            third = list(range(11215, 11259, 5)) +list(range(11300, 11350, 5))

            for i in third:
                if lesson1 == 0:
                    lesson1 = None
                if lesson2 == 0:
                    lesson2 = None

                shedule[i] = {
                    "lesson1": lesson1,
                    "lesson2": lesson2
                }
            return shedule

        def fourth():


            shedule = {}

            lesson1 = int(input("Введите четвертую пару по верхней неделе: "))
            lesson2 = int(input("Введите четвёртую пару по нижней неделе: "))

            fourth = list(range(11400, 11459, 5)) + list(range(11500, 11530, 5))

            for i in fourth:
                if lesson1 == 0:
                    lesson1 = None
                if lesson2 == 0:
                    lesson2 = None

                shedule[i] = {
                    "lesson1": lesson1,
                    "lesson2": lesson2
                }
            return shedule

        def fifth():

            shedule = {}

            lesson1 = int(input("Введите пятую пару по верхней неделе: "))
            lesson2 = int(input("Введите пятую пару по нижней неделе: "))

            fifth = list(range(11540, 11559, 5)) + list(range(11600, 11659, 5))

            for i in fifth:
                if lesson1 == 0:
                    lesson1 = None
                if lesson2 == 0:
                    lesson2 = None

                shedule[i] = {
                    "lesson1": lesson1,
                    "lesson2": lesson2
                }
            return shedule


        def main(self):

            self.shedule = {**first(), **second(), **third(), **fourth(), **fifth()}
            with open("data_lesson.json", "w") as file:
                json.dump(self.shedule, file, indent=4, ensure_ascii=False)
        main()
        

            # with open("data_lesson.json", "w") as file:
            #     json.dump(shedule, file, indent=4, ensure_ascii=False)


    monday()
