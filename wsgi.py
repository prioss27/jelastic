output = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>TestTitle</title>
</head>
<body>
    Hello, World!
</body>
</html>
"""

def application(env, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    yield output.encode("utf-8")
