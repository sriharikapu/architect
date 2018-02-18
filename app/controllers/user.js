/* 
 * app/routes/users.js
 * User routes
 *
 */

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
        }).post(function(req, res, next) {
        // Create new user
        });
};

