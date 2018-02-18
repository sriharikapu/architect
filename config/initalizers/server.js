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

    /* Error Handling */
    app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.json({
        message: err.message,
        error: (app.get('env') === 'development' ? err : {})
    });
        next(err);
    });

    app.listen(config.get('NODE_PORT'));
    logger.info('[SERVER] Listening on port ' + config.get('NODE_PORT'));

    if (cb) {
        return cb();
    }
    
};

