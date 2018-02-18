/*
 * server.js
 * Initalize the Architect server
 *
 */

const express = require("express"),
      path    = require("path");

/* Environment Config */
require("dotenv").config();

/* Middleware */
const bodyParser = require("body-parser"),
      morgan     = require("morgan"),
      logger     = require("winston");

var app;
var start = function(cb) {
    "use strict";

    /* Create Instance of Express server */
    app = express();

    /* Configure Middleware */
    app.use(morgan("dev"));

    app.use(bodyParser.urlencoded({extended: true}));
    app.use(bodyParser.json({type: '*/*'}));

    logger.info('[SERVER] Initializing routes');
    require('../../app/controllers/index')(app);

    /* Error Handling */
    app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.json({
        message: err.message,
        error: (app.get('env') === 'development' ? err : {})
    });
        next(err);
    });

    app.listen(process.env.NODE_PORT);
    logger.info('[SERVER] Listening on port ' + process.env.NODE_PORT);

    if (cb) {
        return cb();
    }
    
};

module.exports = start;

