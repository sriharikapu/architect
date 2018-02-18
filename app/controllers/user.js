/* 
 * app/routes/users.js
 * User routes
 *
 */

const db       = require("../../lib/database"),
      dbPath   = "../database/users/",
      User     = require("../models/user.js");

module.exports = function(router) {
    "use strict";

    /* /users/:user_id */
    router.route('/:userId')
        .get(function(req, res, next) {
        // Return user
        }) 
        .put(function(req, res, next) {
        // Update user
        })
        .patch(function(req, res,next) {
        // Patch
        })
        .delete(function(req, res, next) {
        // Delete record
        });

    router.route('/')
        .get(function(req, res, next) {
        // Logic for GET /users routes
        })
        .post(function(req, res, next) {
        
            var user = User;

            user = {
                id : req.body.id,
                first_name : req.body.first_name,
                last_name : req.body.last_name
            };

            db.saveResource(dbPath, user);

            res.status(200);
            res.json({
                User : user
            });

        });
};

