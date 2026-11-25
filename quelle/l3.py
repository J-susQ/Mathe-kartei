# Level 3: Analysis 2 (Kanon: Forster Analysis 2, Königsberger Analysis 2)
L3 = []
def c(typ, topic, name, back, front="", extra=""):
    L3.append(dict(type=typ, topic=topic, name=name, front=front, back=back, extra=extra, flag=""))

T="Topologie metrischer Räume"
c("Definition",T,r"Offene Kugel / Umgebung",r"In $(X,d)$: $U_r(a)=B_r(a):=\{x\in X: d(x,a)<r\}$. $U\subseteq X$ heißt Umgebung von $a$, wenn ein $r>0$ mit $B_r(a)\subseteq U$ existiert.")
c("Definition",T,r"Offene Menge",r"$U\subseteq X$ heißt offen, wenn zu jedem $a\in U$ ein $\varepsilon>0$ mit $B_\varepsilon(a)\subseteq U$ existiert.",extra=r"Beliebige Vereinigungen und endliche Durchschnitte offener Mengen sind offen. $\bigcap_n(-\frac1n,\frac1n)=\{0\}$ ist nicht offen.")
c("Definition",T,r"Abgeschlossene Menge",r"$A\subseteq X$ heißt abgeschlossen, wenn $X\setminus A$ offen ist. Gleichwertig: Jeder Grenzwert einer konvergenten Folge in $A$ liegt in $A$.")
c("Definition",T,r"Inneres, Abschluss, Rand",r"$\mathring A$ = Vereinigung aller offenen Teilmengen von $A$; $\overline A$ = Durchschnitt aller abgeschlossenen Obermengen; $\partial A=\overline A\setminus\mathring A$.")
c("Definition",T,r"Kompaktheit (Überdeckungskompaktheit)",r"$K\subseteq X$ heißt kompakt, wenn jede offene Überdeckung von $K$ eine endliche Teilüberdeckung besitzt.")
c("Definition",T,r"Folgenkompaktheit",r"$K$ heißt folgenkompakt, wenn jede Folge in $K$ eine Teilfolge besitzt, die gegen einen Punkt aus $K$ konvergiert.",extra=r"In metrischen Räumen sind kompakt und folgenkompakt gleichwertig.")
c("Satz",T,r"Satz von Heine-Borel",r"Eine Teilmenge des $\mathbb R^n$ ist genau dann kompakt, wenn sie beschränkt und abgeschlossen ist.",extra=r"In unendlichdimensionalen Räumen falsch: Die Einheitskugel in $\ell^2$ ist beschränkt und abgeschlossen, aber nicht kompakt.")
c("Satz",T,r"Äquivalenz der Normen auf $\mathbb R^n$",r"Auf einem endlichdimensionalen Vektorraum sind alle Normen äquivalent: Zu $\|\cdot\|,\|\cdot\|'$ gibt es $c,C>0$ mit $c\|x\|\le\|x\|'\le C\|x\|$.")
c("Definition",T,r"Stetigkeit zwischen metrischen Räumen",r"$f:(X,d)\to(Y,d')$ ist stetig in $a$, wenn $\forall\varepsilon\ \exists\delta: d(x,a)<\delta\Rightarrow d'(f(x),f(a))<\varepsilon$.")
c("Satz",T,r"Topologische Charakterisierung der Stetigkeit",r"$f:X\to Y$ ist genau dann stetig, wenn Urbilder offener Mengen offen sind (gleichwertig: Urbilder abgeschlossener Mengen abgeschlossen).")
c("Satz",T,r"",r"$f(K)$ ist kompakt. Ist $Y=\mathbb R$, nimmt $f$ auf $K$ Maximum und Minimum an.",front=r"Sei $f:X\to Y$ stetig und $K\subseteq X$ kompakt.")
c("Definition",T,r"Zusammenhang / Wegzusammenhang",r"$X$ heißt zusammenhängend, wenn $X$ nicht disjunkte Vereinigung zweier nichtleerer offener Mengen ist. $X$ heißt wegzusammenhängend, wenn je zwei Punkte durch einen stetigen Weg $\gamma:[0,1]\to X$ verbunden werden können.",extra=r"Wegzusammenhängend $\Rightarrow$ zusammenhängend. Die Umkehrung gilt nicht (Sinuskurve des Topologen), wohl aber für offene Mengen im $\mathbb R^n$.")
c("Definition",T,r"Kontraktion",r"$f:X\to X$ heißt Kontraktion, wenn es $0\le q<1$ gibt mit $d(f(x),f(y))\le q\,d(x,y)$ für alle $x,y$.")
c("Satz",T,r"Banachscher Fixpunktsatz",r"Sei $(X,d)$ ein vollständiger metrischer Raum ($X\neq\emptyset$) und $f:X\to X$ eine Kontraktion mit Konstante $q<1$. Dann besitzt $f$ genau einen Fixpunkt $x^*$, und für jedes $x_0$ konvergiert $x_{n+1}=f(x_n)$ gegen $x^*$.",extra=r"A-priori-Abschätzung: $d(x_n,x^*)\le\dfrac{q^n}{1-q}d(x_1,x_0)$.")

T="Differentialrechnung im ℝⁿ"
c("Definition",T,r"Partielle Ableitung",r"$f:U\to\mathbb R$, $U\subseteq\mathbb R^n$ offen. $\partial_if(a):=\displaystyle\lim_{h\to0}\frac{f(a+he_i)-f(a)}h$, falls existent.",extra=r"Existenz aller partiellen Ableitungen impliziert nicht einmal Stetigkeit: $f(x,y)=\frac{xy}{x^2+y^2}$, $f(0)=0$.")
c("Definition",T,r"Richtungsableitung",r"$\partial_vf(a):=\displaystyle\lim_{t\to0}\frac{f(a+tv)-f(a)}t$. Ist $f$ differenzierbar, so gilt $\partial_vf(a)=\langle\nabla f(a),v\rangle$.")
c("Definition",T,r"Totale Differenzierbarkeit",r"$f:U\to\mathbb R^m$ heißt in $a$ (total) differenzierbar, wenn es eine lineare Abbildung $A:\mathbb R^n\to\mathbb R^m$ gibt mit $$\lim_{h\to0}\frac{\|f(a+h)-f(a)-Ah\|}{\|h\|}=0.$$ $Df(a):=A$, dargestellt durch die Jacobi-Matrix $\big(\partial_jf_i(a)\big)$.")
c("Satz",T,r"",r"$f$ ist stetig in $a$, alle partiellen Ableitungen existieren, und $Df(a)$ ist die Jacobi-Matrix.",front=r"Sei $f$ in $a$ total differenzierbar.")
c("Satz",T,r"",r"$f$ ist (total) stetig differenzierbar, also insbesondere differenzierbar.",front=r"Seien alle partiellen Ableitungen von $f:U\to\mathbb R^m$ auf $U$ vorhanden und stetig.")
c("Satz",T,r"Kettenregel (mehrdimensional)",r"Ist $f$ in $a$ und $g$ in $f(a)$ differenzierbar, so ist $g\circ f$ in $a$ differenzierbar mit $D(g\circ f)(a)=Dg(f(a))\cdot Df(a)$.")
c("Definition",T,r"Gradient",r"Für differenzierbares $f:U\to\mathbb R$: $\nabla f(a)=\operatorname{grad}f(a)=(\partial_1f(a),\dots,\partial_nf(a))^T$. Er zeigt in Richtung des stärksten Anstiegs.")
c("Satz",T,r"Satz von Schwarz",r"Ist $f:U\to\mathbb R$ zweimal stetig differenzierbar, so gilt $\partial_i\partial_jf=\partial_j\partial_if$ für alle $i,j$. Die Hesse-Matrix ist also symmetrisch.")
c("Satz",T,r"Mittelwertsatz (mehrdimensional)",r"Ist $f:U\to\mathbb R$ differenzierbar und liegt die Strecke $[a,b]$ in $U$, so gibt es $\xi\in[a,b]$ mit $f(b)-f(a)=\langle\nabla f(\xi),b-a\rangle$. Für $f:U\to\mathbb R^m$ gilt nur die Abschätzung $\|f(b)-f(a)\|\le\sup_{\xi}\|Df(\xi)\|\,\|b-a\|$.")
c("Satz",T,r"Taylorformel im $\mathbb R^n$ (2. Ordnung)",r"Für $f\in C^2$: $f(a+h)=f(a)+\langle\nabla f(a),h\rangle+\tfrac12h^THf(a)h+o(\|h\|^2)$, mit der Hesse-Matrix $Hf(a)=(\partial_i\partial_jf(a))$.")
c("Satz",T,r"Notwendige Bedingung für lokale Extrema (mehrdim.)",r"Hat $f:U\to\mathbb R$ in $a\in U$ ein lokales Extremum und ist dort differenzierbar, so ist $\nabla f(a)=0$.")
c("Satz",T,r"Hinreichende Bedingung (Hesse-Matrix)",r"Sei $f\in C^2$, $\nabla f(a)=0$. Ist $Hf(a)$ positiv definit, liegt ein strenges lokales Minimum vor; negativ definit: strenges lokales Maximum; indefinit: Sattelpunkt (kein Extremum).",extra=r"Semidefinit: keine Aussage möglich, z. B. $x^4+y^4$ vs. $x^4-y^4$.")
c("Satz",T,r"Umkehrsatz (Satz über die Umkehrfunktion)",r"Sei $f:U\to\mathbb R^n$ stetig differenzierbar, $U\subseteq\mathbb R^n$ offen und $Df(a)$ invertierbar. Dann gibt es offene Umgebungen $V\ni a$, $W\ni f(a)$, sodass $f:V\to W$ bijektiv ist mit $C^1$-Umkehrung und $D(f^{-1})(f(x))=(Df(x))^{-1}$.",extra=r"Nur lokal: $(r,\varphi)\mapsto(r\cos\varphi,r\sin\varphi)$ hat überall invertierbare Ableitung für $r>0$, ist global aber nicht injektiv.")
c("Satz",T,r"Satz über implizite Funktionen",r"Sei $F:U\subseteq\mathbb R^k\times\mathbb R^m\to\mathbb R^m$ stetig differenzierbar, $F(a,b)=0$ und $D_yF(a,b)$ invertierbar. Dann gibt es Umgebungen $V\ni a$, $W\ni b$ und eine $C^1$-Funktion $g:V\to W$ mit: $F(x,y)=0\Leftrightarrow y=g(x)$ für $(x,y)\in V\times W$. Es gilt $Dg(x)=-\big(D_yF\big)^{-1}D_xF$.")
c("Satz",T,r"Lagrange-Multiplikatoren",r"Hat $f\in C^1$ unter der Nebenbedingung $g(x)=0$ ($g:U\to\mathbb R^m$, $C^1$, $\operatorname{rang}Dg(a)=m$) in $a$ ein lokales Extremum, so gibt es $\lambda_1,\dots,\lambda_m$ mit $\nabla f(a)=\sum_{i}\lambda_i\nabla g_i(a)$.")
c("Definition",T,r"Untermannigfaltigkeit",r"$M\subseteq\mathbb R^n$ heißt $k$-dim. $C^1$-Untermannigfaltigkeit, wenn es zu jedem $a\in M$ eine offene Umgebung $U$ und $g:U\to\mathbb R^{n-k}$ in $C^1$ gibt mit $M\cap U=g^{-1}(0)$ und $\operatorname{rang}Dg=n-k$ auf $M\cap U$.")

T="Kurven"
c("Definition",T,r"Kurve, Tangentialvektor",r"Eine Kurve ist eine stetige Abbildung $\gamma:[a,b]\to\mathbb R^n$. Ist $\gamma$ differenzierbar, heißt $\gamma'(t)$ Tangentialvektor; $\gamma$ heißt regulär, wenn $\gamma'(t)\ne0$ für alle $t$.")
c("Definition",T,r"Rektifizierbarkeit und Bogenlänge",r"$\gamma$ heißt rektifizierbar, wenn $L(\gamma)=\sup_Z\sum_k\|\gamma(t_k)-\gamma(t_{k-1})\|<\infty$ (Supremum über alle Zerlegungen). Für $C^1$-Kurven gilt $L(\gamma)=\int_a^b\|\gamma'(t)\|\,dt$.",extra=r"Nicht rektifizierbar: $\gamma(t)=(t,\,t\cos(\pi/t))$ auf $(0,1]$, $\gamma(0)=0$.")
c("Definition",T,r"Kurvenintegral (über Vektorfeld)",r"Für ein stetiges Vektorfeld $F$ und eine $C^1$-Kurve $\gamma$: $\displaystyle\int_\gamma F\cdot dx:=\int_a^b\langle F(\gamma(t)),\gamma'(t)\rangle\,dt$.")
c("Satz",T,r"Gradientenfelder und Wegunabhängigkeit",r"Ist $F=\nabla\varphi$ ein Gradientenfeld, so gilt $\int_\gamma F\cdot dx=\varphi(\gamma(b))-\varphi(\gamma(a))$. Kurvenintegrale sind dann wegunabhängig, über geschlossene Kurven gleich $0$.",extra=r"Auf sternförmigen Gebieten gilt umgekehrt: $F\in C^1$ mit $\partial_iF_j=\partial_jF_i$ ist ein Gradientenfeld (Lemma von Poincaré).")

T="Gewöhnliche Differentialgleichungen"
c("Definition",T,r"Anfangswertproblem",r"Gegeben $f:D\subseteq\mathbb R\times\mathbb R^n\to\mathbb R^n$ und $(t_0,y_0)\in D$. Gesucht ist eine differenzierbare Funktion $y$ auf einem Intervall um $t_0$ mit $y'(t)=f(t,y(t))$ und $y(t_0)=y_0$.")
c("Definition",T,r"Lokale Lipschitz-Bedingung",r"$f(t,y)$ genügt lokal einer Lipschitz-Bedingung bzgl. $y$, wenn jeder Punkt eine Umgebung $V$ und ein $L$ besitzt mit $\|f(t,y)-f(t,\tilde y)\|\le L\|y-\tilde y\|$ für $(t,y),(t,\tilde y)\in V$.",extra=r"Hinreichend: $f$ stetig partiell nach $y$ differenzierbar.")
c("Satz",T,r"Satz von Picard-Lindelöf",r"Ist $f$ stetig und genügt lokal einer Lipschitz-Bedingung bezüglich $y$, so besitzt das Anfangswertproblem $y'=f(t,y)$, $y(t_0)=y_0$ lokal genau eine Lösung.",extra=r"Beweis: Banachscher Fixpunktsatz für $(Ty)(t)=y_0+\int_{t_0}^tf(s,y(s))\,ds$. Ohne Lipschitz keine Eindeutigkeit: $y'=\sqrt{|y|}$, $y(0)=0$.")
c("Satz",T,r"Existenzsatz von Peano",r"Ist $f$ stetig, so besitzt $y'=f(t,y)$, $y(t_0)=y_0$ lokal mindestens eine Lösung (ohne Eindeutigkeit).")
c("Satz",T,r"Trennung der Variablen",r"Für $y'=g(t)h(y)$ mit $h(y_0)\ne0$ ist die Lösung implizit gegeben durch $\displaystyle\int_{y_0}^{y(t)}\frac{ds}{h(s)}=\int_{t_0}^tg(\tau)\,d\tau$.")
c("Satz",T,r"Lineare DGL erster Ordnung",r"Die Lösung von $y'=a(t)y+b(t)$, $y(t_0)=y_0$ ist $$y(t)=e^{A(t)}\Big(y_0+\int_{t_0}^te^{-A(s)}b(s)\,ds\Big),\quad A(t)=\int_{t_0}^ta(s)\,ds.$$",extra=r"Herleitung: Variation der Konstanten.")
c("Satz",T,r"Lösungsraum linearer Systeme",r"Die Lösungen des homogenen Systems $y'=A(t)y$ ($A$ stetig, $n\times n$) bilden einen $n$-dimensionalen Vektorraum. Jede Lösung des inhomogenen Systems ist spezielle Lösung plus homogene Lösung.")
c("Definition",T,r"Fundamentalsystem und Wronski-Determinante",r"Eine Basis $\varphi_1,\dots,\varphi_n$ des Lösungsraums von $y'=A(t)y$ heißt Fundamentalsystem. $W(t)=\det(\varphi_1(t),\dots,\varphi_n(t))$ heißt Wronski-Determinante.",extra=r"$W$ ist entweder überall $0$ oder nirgends $0$ (Liouville: $W'=\operatorname{tr}A\cdot W$).")
c("Satz",T,r"Lineare Systeme mit konstanten Koeffizienten",r"Die Lösung von $y'=Ay$, $y(0)=y_0$ mit konstanter Matrix $A$ ist $y(t)=e^{tA}y_0$, wobei $e^{tA}=\sum_{k\ge0}\frac{t^kA^k}{k!}$.")
c("Satz",T,r"Lemma von Gronwall",r"Ist $u\ge0$ stetig mit $u(t)\le\alpha+\beta\int_{t_0}^tu(s)\,ds$ für $t\ge t_0$, $\beta\ge0$, so gilt $u(t)\le\alpha e^{\beta(t-t_0)}$.",extra=r"Anwendung: stetige Abhängigkeit vom Anfangswert und Eindeutigkeit.")

T="Integration im ℝⁿ"
c("Satz",T,r"Satz von Fubini",r"Ist $f$ auf $X\times Y\subseteq\mathbb R^{p}\times\mathbb R^q$ integrierbar, so gilt $$\int_{X\times Y}f=\int_X\Big(\int_Yf(x,y)\,dy\Big)dx=\int_Y\Big(\int_Xf(x,y)\,dx\Big)dy.$$",extra=r"Ohne Integrierbarkeit falsch: $f(x,y)=\frac{x^2-y^2}{(x^2+y^2)^2}$ auf $[0,1]^2$ liefert verschiedene iterierte Integrale.")
c("Satz",T,r"Transformationssatz",r"Sei $\Phi:U\to V$ ein $C^1$-Diffeomorphismus offener Mengen im $\mathbb R^n$. Dann ist $f$ genau dann über $V$ integrierbar, wenn $(f\circ\Phi)\,|\det D\Phi|$ über $U$ integrierbar ist, und $$\int_Vf(y)\,dy=\int_Uf(\Phi(x))\,|\det D\Phi(x)|\,dx.$$",extra=r"Polarkoordinaten: $dx\,dy=r\,dr\,d\varphi$. Kugelkoordinaten: $r^2\sin\theta\,dr\,d\theta\,d\varphi$.")
c("Satz",T,r"Prinzip von Cavalieri",r"Für messbares $A\subseteq\mathbb R^{n}$ gilt $\operatorname{vol}_n(A)=\displaystyle\int\operatorname{vol}_{n-1}(A_t)\,dt$, wobei $A_t$ die Schnitte bei fester letzter Koordinate $t$ sind.")
c("Satz",T,r"Vertauschung von Differentiation und Integration (Parameterintegrale)",r"Ist $f(x,t)$ auf $[a,b]\times I$ stetig und $\partial_tf$ stetig, so ist $F(t)=\int_a^bf(x,t)\,dx$ stetig differenzierbar mit $F'(t)=\int_a^b\partial_tf(x,t)\,dx$.")
c("Satz",T,r"Satz von der majorisierten Konvergenz (Lebesgue)",r"Gilt $f_n\to f$ fast überall und $|f_n|\le g$ mit integrierbarem $g$, so ist $f$ integrierbar und $\int f_n\to\int f$.",extra=r"Ohne Majorante falsch: $f_n=n\mathbf 1_{(0,1/n)}\to0$, aber $\int f_n=1$.")
c("Satz",T,r"Satz von der monotonen Konvergenz (Beppo Levi)",r"Ist $0\le f_1\le f_2\le\dots$ messbar mit $f_n\to f$, so gilt $\int f_n\to\int f$ (auch wenn der Wert $\infty$ ist).")
c("Satz",T,r"Gaußscher Integralsatz",r"Sei $G\subseteq\mathbb R^n$ ein kompaktes Gebiet mit glattem Rand und äußerer Einheitsnormale $\nu$, $F$ ein $C^1$-Vektorfeld. Dann $$\int_G\operatorname{div}F\,dx=\int_{\partial G}\langle F,\nu\rangle\,dS.$$")

T="Topologie metrischer Räume"
c("Satz",T,r"Vollständigkeit des $\mathbb R^n$",r"$(\mathbb R^n,\|\cdot\|)$ ist für jede Norm vollständig: Eine Folge konvergiert genau dann, wenn sie komponentenweise konvergiert, und jede Cauchy-Folge konvergiert.")
c("Satz",T,r"Vollständigkeit von $C([a,b])$",r"Der Raum $C([a,b])$ der stetigen Funktionen mit der Supremumsnorm $\|f\|_\infty=\sup|f|$ ist ein Banachraum.",extra=r"Mit der Norm $\|f\|_1=\int_a^b|f|$ ist $C([a,b])$ dagegen nicht vollständig.")
c("Definition",T,r"Operatornorm",r"Für lineares $A:\mathbb R^n\to\mathbb R^m$: $\|A\|:=\sup_{\|x\|\le1}\|Ax\|$. Es gilt $\|Ax\|\le\|A\|\,\|x\|$ und $\|AB\|\le\|A\|\,\|B\|$.",extra=r"Lineare Abbildungen zwischen endlichdimensionalen Räumen sind stets stetig (sogar Lipschitz).")
c("Satz",T,r"",r"$f$ ist auf $K$ gleichmäßig stetig.",front=r"Sei $f:X\to Y$ stetig zwischen metrischen Räumen und $K\subseteq X$ kompakt.")
c("Satz",T,r"",r"Das Bild $f(X)$ ist zusammenhängend.",front=r"Sei $f:X\to Y$ stetig und $X$ zusammenhängend.",extra=r"Für $Y=\mathbb R$ liefert das den Zwischenwertsatz.")

T="Differentialrechnung im ℝⁿ"
c("Satz",T,r"Hurwitz-Kriterium (Sylvester)",r"Eine symmetrische Matrix $A$ ist genau dann positiv definit, wenn alle führenden Hauptminoren $\det(a_{ij})_{i,j\le k}$, $k=1,\dots,n$, positiv sind. Negativ definit: Vorzeichen alternieren, beginnend mit $<0$.")
c("Definition",T,r"Tangentialraum einer Untermannigfaltigkeit",r"Für $M=g^{-1}(0)$ (reguläre Nullstellenmenge) ist $T_aM=\ker Dg(a)$; der Normalraum ist $N_aM=(T_aM)^\perp$, aufgespannt von $\nabla g_1(a),\dots,\nabla g_{n-k}(a)$.")
c("Definition",T,r"Diffeomorphismus",r"Eine bijektive Abbildung $f:U\to V$ zwischen offenen Mengen des $\mathbb R^n$ heißt $C^1$-Diffeomorphismus, wenn $f$ und $f^{-1}$ stetig differenzierbar sind.")

T="Gewöhnliche Differentialgleichungen"
c("Satz",T,r"Reduktion auf Systeme erster Ordnung",r"Die DGL $y^{(n)}=f(t,y,y',\dots,y^{(n-1)})$ ist äquivalent zum System $Y'=F(t,Y)$ mit $Y=(y,y',\dots,y^{(n-1)})$ und $F(t,Y)=(Y_2,\dots,Y_n,f(t,Y))$.")
c("Satz",T,r"Maximale Lösungen (Fortsetzungssatz)",r"Unter den Voraussetzungen von Picard-Lindelöf auf einem Gebiet $D$ existiert eine eindeutige maximale Lösung auf einem offenen Intervall $(t_-,t_+)$. Für $t\to t_+$ verlässt $(t,y(t))$ jedes Kompaktum in $D$; z. B. gilt $\|y(t)\|\to\infty$, falls $D=I\times\mathbb R^n$ und $t_+<\sup I$.",extra=r"$y'=y^2$, $y(0)=1$: Lösung $\frac1{1-t}$ explodiert bei $t=1$.")
c("Definition",T,r"Exakte Differentialgleichung",r"$P(x,y)+Q(x,y)\,y'=0$ heißt exakt, wenn es $F$ mit $\partial_xF=P$, $\partial_yF=Q$ gibt. Lösungen erfüllen dann $F(x,y(x))=\text{const}$.",extra=r"Notwendig (und auf einfach zusammenhängenden Gebieten hinreichend): $\partial_yP=\partial_xQ$.")

T="Integration im ℝⁿ"
c("Definition",T,r"Lebesgue-Nullmenge",r"$N\subseteq\mathbb R^n$ ist eine Nullmenge, wenn es zu jedem $\varepsilon>0$ abzählbar viele Quader $Q_k$ mit $N\subseteq\bigcup Q_k$ und $\sum\operatorname{vol}(Q_k)<\varepsilon$ gibt.",extra=r"$\mathbb Q$ ist eine Nullmenge, ebenso jede abzählbare Menge und jede Hyperebene im $\mathbb R^n$.")
c("Satz",T,r"Lebesgue-Kriterium für Riemann-Integrierbarkeit",r"Eine beschränkte Funktion $f:[a,b]\to\mathbb R$ ist genau dann Riemann-integrierbar, wenn ihre Unstetigkeitsstellen eine Nullmenge bilden.")
