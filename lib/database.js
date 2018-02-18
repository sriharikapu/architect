/*
 * lib/database.js
 * Create filestructure for local db and allow storeage/retrival
 * 
 */

const fs     = require("fs"),
      path   = require("path"),
      logger = require("winston");

module.exports = {
   
    createFilestructure: function(cb) {

        let mkdirSync = function (dirPath) {
            try {
                fs.mkdirSync(dirPath)
            } catch (err) {
                if (err.code !== 'EEXIST') {
                    logger.error(err)
                } 
            }
        };

        mkdirSync(path.resolve("./database"));
        mkdirSync(path.resolve("./database/users"));

        if (cb) {
            return cb(); 
        };

    }

};

