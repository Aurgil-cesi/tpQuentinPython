create table if not exists pypixelart.cell(
    x integer not null,
    y integer not null,
    color integer not null,
    primary key(x, y)
)