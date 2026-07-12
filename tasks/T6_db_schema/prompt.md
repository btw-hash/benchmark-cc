In `schema.prisma`, add a `Post` model and link it to `User` with a one-to-many relation. Requirements:

- `Post` fields: `id` (cuid), `title` (string), `content` (string, optional), `published` (bool, default false), `createdAt`, `updatedAt`, `authorId` (foreign key to User), and the `author` relation.
- `User` should get a `posts Post[]` field.
- Add an index on `Post.authorId` for query performance.
- Add an index on `Post.published` (we'll be filtering by it often).

You can validate the schema with `npx prisma format` and `npx prisma validate` (no DB connection needed for validate).
