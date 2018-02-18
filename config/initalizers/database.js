/*
 * config/initalizers/database
 * Create database
 *
 */

const database = require("../../lib/database");

module.exports = function(cb){

    // create filestructure and pass callback
    database.createFilestructure();

};

