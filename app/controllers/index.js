/*
 * app/routes/index.js
 * Initalizes all routes
 *
 */

const express = require("express"),
      routes = require("require-dir")();

module.exports = function(app) {
    "use strict";

    /* Initalize all routes */
    Object.keys(routes).forEach(function(routeName) {

        var router = express.Router();

        // Initialize the route to add its functionality to router
        require('./' + routeName)(router);
    
        // Add router to the speficied route name in the app
        app.use('/' + routeName, router);         

    });
};

