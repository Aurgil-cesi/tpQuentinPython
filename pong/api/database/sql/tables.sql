create table if not exists pypong.player (
    id integer primary key auto_increment,
    username varchar(50) not null
);

create table if not exists pypong.game(
    id integer primary key auto_increment,
    name varchar(255) not null
);

create table if not exists pypong.game_player(
    game_id integer not null,
    player_id integer not null,
    x integer,
    y integer,
    primary key(game_id, player_id),
    constraint fk_gp_game foreign key (game_id) references pypong.game(id),
    constraint fk_gp_player foreign key (player_id) references pypong.player(id)
);