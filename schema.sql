drop table if exists tracks;
    create table tracks (
        id integer primary key autoincrement,
        title TEXT not null,
        source_audio text not null,
        cover text
    );