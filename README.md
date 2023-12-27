# Урок №10. Словари
## Задание №1
Ранее вы выполняли задание связанное с ветеринарной клиникой. В той задаче вам предстояло вывести информацию о питомце на экран. Сейчас вам необходимо создать словарь pets = {}   
Примерный вид будет следующим:   
pets = {   
  "Имя питомца": {   
    'Вид питомца': # придумайте каким образом сюда внести информацию,   
    'Возраст питомца': # придумайте каким образом сюда внести информацию,   
    'Имя владельца': # придумайте каким образом сюда внести информацию   
  }   
}   
У вас должен получиться словарь, с ещё одним словарём внутри. То есть, есть словарь pets. Он в себе хранит ещё один словарь, который обозначается именем питомца. Имя питомца также нужно каким-то образом вносить туда.   
Задача не будет считаться выполненной, если вы заходите сразу внести информацию, не прибегая в функции input()   
Например:    
pets = {   
  "Мухтар": {   
    "Вид питомца": "Собака",   
    "Возраст питомца": 9,   
    "Имя владельца": "Павел"    
  }   
}   
Так должен будет выглядеть результирующий словарь, но первоначальный его вид - пустой. Его необходимо заполнить пользовательским вводом через консоль с помощью функции input(), а не вписать значения уже в самом коде.   
Возраст питомца должен быть типа int Всё остальное - строки   
Так как возраст питомца указывается типом int. Необходимо, в соответствии с указанным возрастом выводит год, года или лет. Например:   
Его возраст: 24 года    
Его возраст: 21 год    
Его возраст: 19 лет    
И теперь осталось только получить всю информацию о питомце в виде строки, как из задания по Урок №3. Ввод-вывод и базовые переменные. Задание №1, но с небольшими изменениями. Для получения информации необходимо воспользоваться методами словаря keys() и values():   
Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша   
## Задание №2
С помощью цикла создайте словарь, в котором ключи будут, например от числа 10, до -5 (включительно). А значениями этих ключей будут сами эти числа возведенные в степени равных этим числам
Например:   
my_dict = {   
  10: 10000000000,   
  9: 387420489,   
  * и так далее ...   
  -5: -0.00032   
