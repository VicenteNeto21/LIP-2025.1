# Hierarquia de Classes: Personagens de Animes

O codigo foi criado em `java` 

## Classe Base

### Personagem
Representa um personagem genérico de anime com atributos comuns, como `nome` e `nível`, e métodos como `atacar()` e `apresentar()`.

## Subclasses

```text
**Personagem**
├── Ninja
├── Cavaleiro
└── Pirata
```

## Classes:

#### Personagem.java
```Java

public class Personagem {
    protected String nome;
    protected int nivel;

    public Personagem(String nome, int nivel) {
        this.nome = nome;
        this.nivel = nivel;
    }

    public void atacar() {
        System.out.println(nome + " atacou!");
    }

    public void apresentar() {
        System.out.println("Sou " + nome + ", nível " + nivel + ".");
    }
}

```
#### Ninja.java

```Java

public class Ninja extends Personagem {
    private String aldeia;

    public Ninja(String nome, int nivel, String aldeia) {
        super(nome, nivel);
        this.aldeia = aldeia;
    }

    @Override
    public void atacar() {
        System.out.println(nome + " lançou um jutsu secreto da Aldeia " + aldeia + "!");
    }
}

```

#### Cavaleiro.java

```Java

public class Cavaleiro extends Personagem {
    private String armadura;

    public Cavaleiro(String nome, int nivel, String armadura) {
        super(nome, nivel);
        this.armadura = armadura;
    }

    @Override
    public void atacar() {
        System.out.println(nome + " usou o golpe sagrado com a armadura de " + armadura + "!");
    }
}

```


#### Pirata.java

```Java

public class Pirata extends Personagem {
    private String frutaDoDiabo;

    public Pirata(String nome, int nivel, String frutaDoDiabo) {
        super(nome, nivel);
        this.frutaDoDiabo = frutaDoDiabo;
    }

    @Override
    public void atacar() {
        System.out.println(nome + " ativou o poder da fruta " + frutaDoDiabo + "!");
    }
}

```

#### Main.java

```Java

public class Main {
    public static void main(String[] args) {
        Ninja naruto = new Ninja("Naruto", 50, "Folha");
        Cavaleiro seiya = new Cavaleiro("Seiya", 45, "Pégaso");
        Pirata luffy = new Pirata("Luffy", 55, "Gomu Gomu");

        naruto.apresentar();
        naruto.atacar();

        seiya.apresentar();
        seiya.atacar();

        luffy.apresentar();
        luffy.atacar();
    }
}

```

## Resultado Esperado

```Java
Sou Naruto, nível 50.
Naruto lançou um jutsu secreto da Aldeia Folha!
Sou Seiya, nível 45.
Seiya usou o golpe sagrado com a armadura de Pégaso!
Sou Luffy, nível 55.
Luffy ativou o poder da fruta Gomu Gomu!
```