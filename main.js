/*
 * main.js
 * Entry point for the Architect backend
 *
 */

"use strict";

const server = require("./config/initalizers/server"),
      async  = require("async"),
      logger = require("winston");

// load environment variables from .env
require("dotenv").config();

// Initalize Modules
async.series([
    function startServer(callback) {
        server(callback);
    }], function(err) {
        if (err) {
            logger.error(err);
        } else {
            logger.info("[SERVER] Initalized Sucessfully");
        }
    }
);

