FROM ruby:3.4.5 as builder
WORKDIR /app
COPY Gemfile ./
RUN bundle config set without 'test' && \
    bundle install
COPY . .
RUN JEKYLL_ENV=production bundle exec jekyll build

FROM nginx:1.29.0-alpine
COPY --from=builder /app/_site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]