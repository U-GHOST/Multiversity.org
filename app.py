#!/usr/bin/env python3

# Multiversity.org

from flask import (
	Flask,
	render_template
)

app = Flask(
	__name__,
	template_folder = "./templates",
    static_folder = "./static"
)

@app.route( "/" )
@app.route( "/index.html" )
def home():
    return render_template( "index.html" )

@app.route( "/world-one" )
@app.route( "/world-one.html" )
def worldOne():
    return render_template( "world-one.html" )

@app.route( "/world-two" )
@app.route( "/world-two.html" )
def worldTwo():
    return render_template( "world-two.html" )

@app.route( "/world-three" )
@app.route( "/world-three.html" )
def worldThree():
    return render_template( "world-three.html" )

@app.route( "/space" )
@app.route( "/space.html" )
def space():
    return render_template( "space.html" )

if __name__ == "__main__":
    app.run( debug = True )
