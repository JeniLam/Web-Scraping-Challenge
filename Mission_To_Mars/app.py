from flask import Flask, render_template, redirect
import scrape_mars

app = Flask(__name__)