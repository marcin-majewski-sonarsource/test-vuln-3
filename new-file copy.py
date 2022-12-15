from flask import request
print 'new-test'
print 'test'
print 'test-2'
@app.route('/')
def index():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\
    
@app.route('/')
def index2():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\
    
@app.route('/')
def index3():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\
    console.log("test")


@app.route('/')
def index4():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\

@app.route('/')
def index5():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\

@app.route('/')
def index6():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\

@app.route('/')
def index7():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\
