/*
 * main.js
 * Entry point for the Architect backend
 *
 */

"use strict";

const server = require("./config/initalizers/server");

// load environment variables from .env
require("dotenv").loads();

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
