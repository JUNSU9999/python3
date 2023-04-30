#! C:\Python311\python.exe
import cgi, os, view

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
if "id" in form:
    pageId = form["id"].value
    description = open("data/" + pageId, "r", encoding="utf-8").read()
else:
    pageId = "Welcome"
    description = "Hello web"
print(
    """<!DOCTYPE html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset = "utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
""".format(
        title=pageId, desc=description, listStr=view.getList()
    )
)
