# Python
task 1 

На вход программе подаются два массива целых чисел, разделённых пробелом. Необходимо найти число вхождений второго
массива в первый. То есть посчитать, сколько раз последовательность чисел второго массива (без перестановок) встречается в
первом.

task 2

Имеется сервер, имеющий М каналов для подключений клиентов. Когда клиент не подключен к каналу, канал простаивает. Когда к
каналу подключен клиент, он считается занятым, и к нему нельзя подключиться. Каждый канал ведет текстовый лог подключений/
отключений клиентов, следующего вида:

4 22 9 <...>

Каждая запись данного лога - это временная метка в секундах от старта сервера. Нечетные записи (по порядку, а не по значению) р
подключения, четные - отключения. В данном примере имеем лог канала, к которому на 4-ой секунде подключился клиент, на 22
секунде - отключился, и на 59 секунде - подключился, то есть сейчас этот канал занят.

Для определенности все эти периоды являются полуинтервалами: левая граница включена в период подключения, а правая не
включена. Т.е. если лог имеет вид 1 2 2 4, то это значит что канал был занят с 1 по 4 секунду.

Необходимо имея логи всех каналов, определить периоды когда все каналы были заняты.

Формат описания входных данных:
В первой строке записано количество каналов М. В следующих строках описания каждого из М логов.
Каждое описание логов состоит из двух строк:

- кол-во записей в логе
- записи в логе, разделенные пробелом

Гарантируется, что в каждом логе четное количество записей и что лог отсортирован в неубывающем порядке.
