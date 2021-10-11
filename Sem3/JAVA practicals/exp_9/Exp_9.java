

public class Exp_9  {
    public static void main(String[] args) {
        Aniko a = new Aniko("JoJo's the bizarre adventure", "Action, Adventure and Comedy", 2012, 24);
        a.display();
        }   

    }


 interface Info{
    public void genre(String g);
    public void release_date(int r);
    public void episodes(int e);
}
 interface Name{
    public void name(String n);
}

interface Anime extends Info,Name{
 public void display();
}

class Aniko implements Anime{
    private String genr,name_1;
    private int releasedate,episode;
    public void genre(String genr){
        this.genr = genr;
    }
    public void name(String name_1){
        this.name_1 = name_1;
    }
    public void episodes(int episode){
        this.episode = episode;
    }
    public void release_date(int r){
        this.releasedate = r;
    }
    public Aniko(String name,String genre,int release_date, int episodes){
        genre(genre);
        name(name);
        release_date(release_date);
        episodes(episodes);
    }
    public void display(){
        System.out.println("Name: "+this.name_1+" Genre: "+this.genr+" Release date: "+this.releasedate+" No. of episodes: "+this.episode);
    }
}