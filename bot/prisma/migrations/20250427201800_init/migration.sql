-- CreateTable
CREATE TABLE "Fan" (
    "id" TEXT NOT NULL,
    "whatsapp_number" TEXT NOT NULL,
    "nome" TEXT NOT NULL,
    "cidade" TEXT NOT NULL,
    "cpf" TEXT,
    "prefere_alerta_jogos" BOOLEAN NOT NULL DEFAULT false,
    "prefere_novidades" BOOLEAN NOT NULL DEFAULT false,
    "redes_sociais" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Fan_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Interaction" (
    "id" TEXT NOT NULL,
    "fanId" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Interaction_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Notification" (
    "id" TEXT NOT NULL,
    "fanId" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "status" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Notification_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "FanSegment" (
    "id" TEXT NOT NULL,
    "fanId" TEXT NOT NULL,
    "cluster" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "FanSegment_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "KPIReport" (
    "id" TEXT NOT NULL,
    "data" TIMESTAMP(3) NOT NULL,
    "total_fans" INTEGER NOT NULL,
    "opt_in_jogos" DOUBLE PRECISION NOT NULL,
    "opt_in_promo" DOUBLE PRECISION NOT NULL,
    "engajamento" DOUBLE PRECISION NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "KPIReport_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Fan_whatsapp_number_key" ON "Fan"("whatsapp_number");

-- AddForeignKey
ALTER TABLE "Interaction" ADD CONSTRAINT "Interaction_fanId_fkey" FOREIGN KEY ("fanId") REFERENCES "Fan"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Notification" ADD CONSTRAINT "Notification_fanId_fkey" FOREIGN KEY ("fanId") REFERENCES "Fan"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "FanSegment" ADD CONSTRAINT "FanSegment_fanId_fkey" FOREIGN KEY ("fanId") REFERENCES "Fan"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
