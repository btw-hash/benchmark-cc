The Express app in `server.js` supports POST/GET/DELETE for users. Add a `PATCH /users/:id` route that allows partial updates.

Requirements (verified by `server.test.js`):
- Updates only the provided fields (`name` and/or `email`).
- Returns 404 if the user does not exist.
- Returns 400 if the body is empty or contains unknown fields.
- Must not allow changing `id`.
- Returns the updated user as JSON on success.

Run `npm install` then `npm test`. Do not modify the test file.
