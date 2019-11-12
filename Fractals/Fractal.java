package fractal;

import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
 
public class Fractal extends JFrame {

	public Fractal() {
		setBounds(0,0,1000,800);
		setResizable(false);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	public void drawTree(Graphics g, int x0, int y0, double angle, double len) {
		if(len <= 2) return;
		int x1 = x0 + (int)(Math.cos(Math.toRadians(angle)) * len * 10.0);
		int y1 = y0 - (int)(Math.sin(Math.toRadians(angle)) * len * 10.0);
        g.drawLine(x0, y0, x1, y1);
		drawTree(g, x1, y1, angle + (3 * len), len - 1);
		drawTree(g, x1, y1, angle - len * 1.5, len - 1);

	}	
	
	@Override
	public void paint(Graphics g) {
		g.setColor(Color.BLACK);
		drawTree(g, 500, 700, 90, 10);
	}
	
	public static void main(String[] args) {
		new Fractal().setVisible(true);
	}

}
