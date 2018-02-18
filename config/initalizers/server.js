/*
 * server.js
 * Initalize the Architect server
 *
 */

const express = require("express");
const path    = require("path");

/* MIDDLEWARE */
const bodyParser = require("body-parser");
const morgan     = require("morgan");
const logger     = require("winston");

var app;

export start = function(cb) {
    "use strict";

    /* Create Instance of Express server */
    app = express();

    /* Configure Middleware */
    app.use(morgan("dev"));

    app.use(bodyParser.urlencoded({extended: true}));
    app.use(bodyParser.json({type: '*/*'}));

};

