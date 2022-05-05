"""3.	Company model.
Используя ООП, необходимо промоделировать взаимодействие компании со своими сотрудниками.
Обратите внимание на файл business_original.py. В нем содержатся некоторые шаблоны, которые необходимо реализовать

Релизуйте следующую модель:

Класс Company
•	у компании есть название и адрес
•	у компании есть список сотрудников (employees)
•	сотрудником компании может стать только менеджер или инженер
•	компания может уволить любого сотрудника
•	стартовый капитал у компании 1000 монет (money)
•	компания платит сотрудникам за работу
•	когда в компании праздник - каждый сотрудник получает по 5 монет
•	когда у компании заканчиваются деньги - она становится банкротом, а все ее сотрудники безработными

Класс Person
•	у человека есть имя и возраст. Также могут быть указаны адрес и пол

Класс Employee (базовый класс для сотрудников, наследуется от Person)
•	employee может быть нанятым в компанию или быть безработрым
•	employee может работать только в 1-й компании
•	employee не может работать, если он безработный
•	стартовый капитал у employee 0 монет

Класс Engineer (наследуется от Employee)
•	инженер зарабатывает 10 монет за работу. Деньги снимаются с баланса компании и прибавляются инженеру

Класс Manager (наследуется от Employee)
•	за работу менеджер получает 12 монет. Деньги снимаются с баланса компании и прибавляются менеджеру
"""

from business import check_yourself

check_yourself()
