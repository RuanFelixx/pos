from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Pedido(SQLModel, table=True):
    IdPedido: Optional[int] = Field(default=None, primary_key=True)
    ProtocoloPedido: str
    Esfera: str
    UF: Optional[str]
    Municipio: Optional[str]
    OrgaoDestinatario: str
    Situacao: str
    DataRegistro: Optional[date]
    PrazoAtendimento: Optional[date]
    FoiProrrogado: Optional[str]
    FoiReencaminhado: Optional[str]
    FormaResposta: str
    OrigemSolicitacao: str
    IdSolicitante: Optional[int]
    AssuntoPedido: str
    SubAssuntoPedido: str
    Tag: Optional[str]
    DataResposta: Optional[date]
    Decisao: Optional[str]
    EspecificacaoDecisao: Optional[str]
