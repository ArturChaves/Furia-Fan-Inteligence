/*
  Warnings:

  - Changed the type of `cluster` on the `FanSegment` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.

*/
-- AlterTable
ALTER TABLE "FanSegment" DROP COLUMN "cluster",
ADD COLUMN     "cluster" INTEGER NOT NULL;
