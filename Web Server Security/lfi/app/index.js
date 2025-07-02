const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const { ApolloServerPluginLandingPageDisabled } = require('apollo-server-core');
const { readFileSync } = require('fs');
const { join } = require('path');
const app = express();

const schema = readFileSync(join(__dirname, 'graphql/schema.gql'), 'utf-8');

const resolvers = require('./graphql/resolvers');

const server = new ApolloServer({ 
  typeDefs: schema, 
  resolvers,
  plugins: [ApolloServerPluginLandingPageDisabled()],
});

async function startServer() {
  // Await the server start
  await server.start();

  server.applyMiddleware({ app });
  app.use(express.static('public'));

  // Define endpoint /getPicture
  app.get('/getPicture', (req, res) => {
    const { file } = req.query;
    if (!file) {
      return res.status(400).json({ error: 'File parameter is required' });
    }

    const filePath = join(__dirname, 'public', 'families', file);

    res.sendFile(filePath);
  });
  
  app.listen({ port: 4000 }, () => {
    console.log(`Server is running`);
  });
}

startServer();
