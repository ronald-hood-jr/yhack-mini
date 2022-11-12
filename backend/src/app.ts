import express, { NextFunction, Request, Response } from "express";
import dotenv from "dotenv";
import { Pool } from "pg";
import { Sequelize, DataTypes } from "sequelize";

const app = express();
dotenv.config();

app.get("/test", (req: Request, res: Response, next: NextFunction) => {
  res.send("hi");
});

app.listen(process.env.PORT, () => {
  console.log(`Server is running at ${process.env.PORT}`);
});

const sequelize = new Sequelize(
  process.env.DB_NAME!,
  process.env.DB_USER!,
  process.env.DB_PASSWORD!,
  {
    host: "postgres",
    dialect: "postgres",
    port: Number(process.env.DB_PORT),
  }
);

const connectToDB = async () => {
  try {
    await sequelize.authenticate();
    console.log("Connection has been established successfully.");
  } catch (error) {
    console.error("Unable to connect to the database:", error);
  }
};
connectToDB();

const Lead = sequelize.define(
  "Lead",
  {
    // Model attributes are defined here
    address: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    owner: {
      type: DataTypes.STRING,
      // allowNull defaults to true
    },
    phone: {
      type: DataTypes.STRING,
    },
    email: {
      type: DataTypes.STRING,
    },
    link: {
      type: DataTypes.STRING,
    },
  },
  {
    // Other model options go here
  }
);

const syncLeads = async () => {
  await Lead.sync({ force: true });
  console.log("The table for the Lead model was just (re)created!");
  const house1 = await Lead.create({
    address: "123 myHouse Ln",
    owner: "Ronald",
    phone: "832-603-9998",
    email: "ronald@gmail.com",
    link: "linktohouse.com",
  });
  console.log(house1 instanceof Lead);

  const leads = await Lead.findAll();
  console.log(leads.every((lead) => lead instanceof Lead)); // true
  console.log("All users:", JSON.stringify(leads, null, 2));
};

syncLeads();
