#!/usr/bin/env python

def headerHTML():
    with open("index.html", "w+") as origHTML:
        origHTML.write("""
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <meta name="robots" content="noindex, nofollow">
  <meta name="googlebot" content="noindex, nofollow">

  <script type="text/javascript" src="/js/lib/dummy.js"></script>
    <link rel="stylesheet" type="text/css" href="/css/result-light.css">

  <style type="text/css">
    @import url(http://fonts.googleapis.com/css?family=Lato:400,900);

.square {
    float:left;
    position: relative; /*relative, absolute*/
    width:5em;
    padding-bottom: 5em;
    margin:.50%;
    background-position:center center;
    background-repeat:no-repeat;
    background-size:cover; /* you change this to "contain" if you don't want the images to be cropped */
}
""")

def variableHTML():
    with open("hardcodedwebsites.txt", "r+") as customWebsites:
        lines = customWebsites.readlines()
        customWebsites.close()

    with open("index.html", 'a') as appendIndex:
        x = 0
        favIcon = "https://icons.better-idea.org/icon?size=80..120..200&url="
        for each in lines:
            appendIndex.write(".img_0-%s{background-image:url('%s%s');}\n" % (x, favIcon, each.rstrip('\n')))
            x += 1
        appendIndex.write("""
body {
    float:center;
    font-size:20px;
    font-family: 'Lato',verdana, sans-serif;
    color: #fff;
    text-align:center;
    background:#ECECEC;
}

</style>
<title>Symbaloo Knockoff</title>
</head>

<body>

  <center>
""")
        x = 0
        for each in lines:
          appendIndex.write("""  <a href='%s'><div class="square img_0-%s"></div></a>
""" % (each.rstrip('\n'), x))
          x+=1

def footerHTML():
    with open("index.html", "a") as footerHTML:
        footerHTML.write("""  </center>

</body>
</html>
""")

headerHTML()
variableHTML()
footerHTML()
