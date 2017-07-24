//
    var k=1;
	var a1 = [108,108,108,108,108,108,108,120,136,143,148,155,161,167];
	var a2 = [134,142,144,147,149,151,154,157,161,166,169,171,173,174];
	var b1 = [9.6,7.7,6.5,5.6,5.0,3.8,2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	var b2 = [25.0,25.0,20.0,16.7,14.3,12.7,10.6,9.9,9.3,8.5,8.1,7.9,7.8,7.7];
	//
	var g_index = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"];
	var gx = [110,112,114,116,120,124, 128,134,140,147,152,156,160,164,170];
	var gy = [14.5,12.0,10.5,9.5,8.8, 8.2, 7.2,5.5,4.0,3.5,3.3,2.8,2.5,2.3,2.2];
	var syllable = 150;
	var sentence = 4.2;
	//
//function doit1(rx) {
//  syllable = rx;
//  draw();
// }
//
// function doit2(ry) {
//  sentence = ry;
//  draw();
// }
//
function drawLine(x1,y1,x2,y2) { 
	var canvas = document.getElementById('fry1');  
        	if (canvas.getContext){  
                       var gS2 = canvas.getContext('2d');  
            	}  
	gS2.lineWidth=1;
	gS2.beginPath();  
	gS2.moveTo(x1,y1);
	gS2.lineTo(x2,y2);
	gS2.closePath;
  	gS2.stroke();
}
//
function drawRect(x1,y1,x2,y2) {
	var canvas = document.getElementById('fry1');  
        	if (canvas.getContext){  
                        var gS2 = canvas.getContext('2d');  
            	}  
                    gS2.beginPath();
	gS2.moveTo(x1,y1);
	gS2.lineTo(x1+x2,y1);
	gS2.lineTo(x1+x2,y1+y2);
	gS2.lineTo(x1,y1+y2);
	gS2.closePath();
	gS2.stroke();
}
//
function draw() {  
        var canvas = document.getElementById('fry1');  
        if (canvas.getContext){  
               	var gS2 = canvas.getContext('2d');  
        }  
			//
			// Coordinate system
			// 
			gS2.fillStyle = "rgb(255,255,255)";
			gS2.fillRect(0,0,500,400);
			//
			gS2.fillStyle = "rgb(240,240,240)";
			gS2.fillRect(0,0,500,20);
			//
			gS2.strokeStyle = "rgb(164,164,164)";
			gS2.lineWidth=2;
			drawLine(0,21,500,21);
			//
			//  chart
			//
			gS2.strokeStyle = "rgb(100,150,220)";
			drawRect(80,100,340,250);
			gS2.fillStyle = "rgb(240,240,240)";
			gS2.fillRect(81,101,338,248);
			gS2.strokeStyle = "rgb(255,255,255)";
			//
			gS2.lineWidth=1;
			for (i=0;i<260;i=i+10) {
			    drawLine(81,100+i,419,100+i);
			}
			for (i=10;i<350;i=i+10) {
			    drawLine(80+i,101,80+i,349);
			}
			//
			gS2.fillStyle = "rgb(0,0,128)";
			gS2.font = "bold 10px Arial"; 
			for (i=108;i<180;i=i+4) {
			  width = gS2.measureText(i+"").width;
			  gS2.fillText(i+"",(-455+i*5)-width,365);
			}
			//
			for (i=1;i<26;i=i+1) {
			  width = gS2.measureText(i+"").width;
			  gS2.fillText(i+"",75-width,355-i*10);
			}
			gS2.strokeStyle = "rgb(0,0,128)";
			for (i=0;i<14;i++) {
			drawLine(-460+(a1[i]*5),350-(b1[i]*10),-460+(a2[i]*5),350-(b2[i]*10))
			}
			gS2.fillStyle = "rgb(128,0,0)";
			gS2.font = "bold 12px Arial"; 
			for (i=0;i<15;i++) {
			gS2.fillText(g_index[i],-455+(gx[i]*5),355-(gy[i]*10));
			}
			//
			gS2.fillStyle = "rgb(100,150,220)";
			gS2.beginPath();
			gS2.moveTo(80,308);
			gS2.lineTo(160,350);
			gS2.lineTo(80,350);
			gS2.closePath();
			gS2.fill();
			//
			gS2.fillStyle = "rgb(100,150,220)";
			gS2.beginPath();
			gS2.moveTo(420,100);
			for (i=1;i<15;i++) {
			gS2.lineTo(-460+(a2[i]*5),350-(b2[i]*10));
			}
			gS2.lineTo(420,352-(7.8*10));
			gS2.closePath();
			gS2.fill();
			//
			gS2.strokeStyle = "rgb(0,0,0)";
			gS2.lineWidth=1;
			drawLine(-460+(syllable*5),101,-460+(syllable*5),349);
			drawLine(81,350-(sentence*10),419,350-(sentence*10));
			gS2.fillStyle = "rgb(225,0,0)";
			gS2.fillRect(-464+(syllable*5),346-(sentence*10),8,8);
			gS2.fillStyle = "rgb(255,255,255)";
			gS2.fillRect(-461+(syllable*5),349-(sentence*10),2,2);
			//
			gS2.fillStyle = "rgb(255,255,255)";
			gS2.font = "bold 12px Arial";
			gS2.fillText("long words", 330,180);
			gS2.font = "bold 10px Arial";
			gS2.fillText("long",83,333);
			gS2.fillText("sentences",83,345);
			//
			gS2.font = "bold 14px Arial";
			gS2.fillStyle = "rgb(128,0,0)";
			gS2.fillText("Fry Readability Index",200,15);
			// gS2.fillText("Average Number of Syllables per 100 words: "+syllable,100,40);
			// gS2.fillText("Average Number of Sentences per 100 words: "+sentence,90,55);
			// gS2.fillText("FKRA Reading Age: ",100,70);
			gS2.font = "bold 12px Arial";
			gS2.fillText("Average Number of Syllables per 100 words",100,390);
			gS2.fillText("Average Number of Sentences per 100 words",50,92);
	}  