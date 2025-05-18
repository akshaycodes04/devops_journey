#1 Use official nginx image as base
FROM nginx:alpine

# Copy your html file to nginx's default html directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start nginx server (this is the default command for nginx image)
CMD ["nginx", "-g", "daemon off;"]

