# mysql.connector هنا قمنا بتضمين كل محتوى الموديول
import mysql.connector

# MySQL حتى ترجع كائن يسمح لنا بالإتصال بقواعد بيانات connect() هنا قمنا باستدعاء الدالة
db = mysql.connector.connect(
  user='root',
  passwd='',
  host='127.0.0.1',
  database='company'
)

# يسمح لنا بالتعامل مع قاعدة البيانات cursor لإنشاء كائن cursor() هنا قمنا باستدعاء الدالة
cursor = db.cursor()

# 'employee' وضعنا فيه نص الإستعلام الذي يسمح بإضافة سطر جديد في الجدول sql المتغير
sql = 'INSERT INTO employee(name, phone) values (%s, %s)'

# يمثل القيم التي ستوضع بالترتيب في الجدول tuple عبارة عن val الكائن
val = ('Ahmad', '96101200155')

# sql و تمرير نص الإستعلام المخزن في المتغير execute() هنا قمنا باستدعاء الدالة
# val و من ثم القيم التي سيتم دمجها مع نص الإستعلام و التي قمنا بتخزينها في الكائن
cursor.execute(sql, val)

# لحفظ التغيرات التي تم إجراءها في قاعدة البيانات commit() هنا قمنا باستدعاء الدالة
db.commit()

# هنا قمنا بطباعة عدد الأسطر التي تم إضافتها في الجدول بسبب الإستعلام الذي تم إرساله سابقاً
print(cursor.rowcount, 'record(s) inserted')

# هنا قمنا بإغلاق الإتصال مع قاعدة البيانات
cursor.close()
db.close()
