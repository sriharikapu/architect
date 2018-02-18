/*
 * main.js
 * Entry point for the Architect backend
 *
 */

"use strict";

const server = require("./config/initalizers/server"),
      async  = require("async");

// load environment variables from .env
require("dotenv").config();

// Initalize Modules
async.series([
    function startServer(callback) {
        server(callback);
    }], function(err) {
        if (err) {
            console.log(err); 
        } else {
            console.log("[Architect] Initalized Successfully"); 
        }
    }
);
