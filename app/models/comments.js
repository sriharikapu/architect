/*
 * app/models/comments.js
 * Comment schema
 *
 */

var Comment = {
    proposal_id    : 0,
    parent_id      : 0,
    user_id        : "",
    selection_text : "",
    body           : "",
};

module.exports = Comment;

