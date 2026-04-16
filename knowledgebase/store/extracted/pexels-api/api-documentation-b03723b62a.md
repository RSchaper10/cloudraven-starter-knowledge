# Pexels API Documentation

Source URL:

- https://www.pexels.com/api/documentation/

Dependency:

- Pexels API

Collected at:

- 2026-04-16T01:15:00+00:00

Direct links in scope:

- https://www.pexels.com/api/documentation/
- https://api.pexels.com/v1/search
- https://api.pexels.com/v1/curated
- https://api.pexels.com/v1/photos/:id
- https://api.pexels.com/v1/videos/
- https://api.pexels.com/v1/videos/search
- https://api.pexels.com/v1/videos/popular
- https://api.pexels.com/v1/videos/videos/:id
- https://api.pexels.com/v1/collections/featured
- https://api.pexels.com/v1/collections
- https://api.pexels.com/v1/collections/:id

Captured summary:

- Manual source import created from pasted official Pexels API documentation because the live documentation page returned a Cloudflare challenge to automated requests.
- The API is a RESTful JSON surface for free stock photos, videos, and collections, with required attribution practices, API-key authorization, pagination, and rate-limit headers.
- Core photo endpoints cover search, curated feeds, and single-photo retrieval; core video endpoints cover search, popular feeds, and single-video retrieval; collections endpoints expose featured, personal, and collection-media views.
- The docs emphasize linking back to Pexels, crediting photographers when possible, avoiding replication of core Pexels functionality, and tracking quota usage with rate-limit headers.

Extracted text:

Pexels API documentation

Capture note: manual paste supplied by user because direct fetch returned a Cloudflare challenge.

Introduction

The Pexels API enables programmatic access to the Pexels content library, including photos, videos, and collections. It is a RESTful JSON API and can be used from any language or framework with HTTP support. Official client libraries are available for Ruby, JavaScript, and .NET.

Important note:

- Video endpoints are now available at `https://api.pexels.com/v1/videos/`.
- The older `https://api.pexels.com/videos/` endpoints are deprecated.

Guidelines

- Show a prominent link to Pexels for API-powered content.
- Credit photographers whenever possible.
- Do not copy or replicate the core functionality of Pexels.
- Default rate limits are 200 requests per hour and 20,000 requests per month.
- Successful responses include `X-Ratelimit-Limit`, `X-Ratelimit-Remaining`, and `X-Ratelimit-Reset`.

Authorization

All requests require an API key sent in the `Authorization` header.

Example:

```bash
curl -H "Authorization: YOUR_API_KEY" \
  "https://api.pexels.com/v1/search?query=people"
```

Pagination

Paginated endpoints accept `page` and `per_page`, with a maximum `per_page` value of `80`. Responses can include `prev_page` and `next_page`.

Example:

```text
GET https://api.pexels.com/v1/curated?page=2&per_page=40
```

Photo resource

Photo objects include:

- `id`
- `width`
- `height`
- `url`
- `photographer`
- `photographer_url`
- `photographer_id`
- `avg_color`
- `src`
- `alt`

The `src` object provides multiple sizes including `original`, `large2x`, `large`, `medium`, `small`, `portrait`, `landscape`, and `tiny`.

Photo endpoints

- `GET https://api.pexels.com/v1/search`
- `GET https://api.pexels.com/v1/curated`
- `GET https://api.pexels.com/v1/photos/:id`

Photo search parameters

- `query` required
- `orientation` optional: `landscape`, `portrait`, `square`
- `size` optional: `large`, `medium`, `small`
- `color` optional: named colors or hex values
- `locale` optional
- `page` optional
- `per_page` optional, default `15`, max `80`

Photo search response fields

- `photos`
- `page`
- `per_page`
- `total_results`
- `prev_page`
- `next_page`

Curated photos

`GET https://api.pexels.com/v1/curated`

Returns a curated set of real-time photos from the Pexels team.

Get a photo

`GET https://api.pexels.com/v1/photos/:id`

Returns a single Photo object.

Video resource

Video objects include:

- `id`
- `width`
- `height`
- `url`
- `image`
- `duration`
- `user`
- `video_files`
- `video_pictures`

Video endpoints

- `GET https://api.pexels.com/v1/videos/search`
- `GET https://api.pexels.com/v1/videos/popular`
- `GET https://api.pexels.com/v1/videos/videos/:id`

Video search parameters

- `query` required
- `orientation` optional: `landscape`, `portrait`, `square`
- `size` optional: `large`, `medium`, `small`
- `locale` optional
- `page` optional
- `per_page` optional, default `15`, max `80`

Video search response fields

- `videos`
- `url`
- `page`
- `per_page`
- `total_results`
- `prev_page`
- `next_page`

Popular videos

`GET https://api.pexels.com/v1/videos/popular`

Supports optional filters for `min_width`, `min_height`, `min_duration`, `max_duration`, `page`, and `per_page`.

Get a video

`GET https://api.pexels.com/v1/videos/videos/:id`

Returns a single Video object.

Collections

Collections group photos and videos into a unified gallery. They cannot be created or modified through the API; the API exposes featured collections and the authenticated user's collections.

Collection resource fields

- `id`
- `title`
- `description`
- `private`
- `media_count`
- `photos_count`
- `videos_count`

Collection endpoints

- `GET https://api.pexels.com/v1/collections/featured`
- `GET https://api.pexels.com/v1/collections`
- `GET https://api.pexels.com/v1/collections/:id`

Collection media parameters

- `type`: `photos` or `videos`
- `sort`: `asc` or `desc`
- `page`
- `per_page`

Collection media response fields

- `id`
- `media`
- `page`
- `per_page`
- `total_results`
- `prev_page`
- `next_page`

Example JavaScript usage

```js
import { createClient } from "pexels";

const client = createClient("YOUR_API_KEY");

client.photos.search({ query: "Nature", per_page: 1 }).then((photos) => {
  // ...
});

client.photos.curated({ per_page: 1 }).then((photos) => {
  // ...
});

client.photos.show({ id: 2014422 }).then((photo) => {
  // ...
});

client.videos.popular({ per_page: 1 }).then((videos) => {
  // ...
});
```
