/**
 * Created by Sancho on 23.02.2015.
 */
import java.util.Scanner;

public class Matrix {

   private int setMatrixSize(){
       int a;
       Scanner in = new Scanner(System.in);
       System.out.println("Enter the size of matrix: ");

       a = in.nextInt();
       if (a<=0){
           System.out.println("Size should be bigger than 0");
           System.exit(0);
       }
       return a;

   }

    private int matrixSize = setMatrixSize() ;
    private float[][] matrix = new float[matrixSize][matrixSize];
    private float[] freeMembers = new float[matrixSize];
    private float[] answers = new float[matrixSize];
    private float[][] l = new float[matrixSize][matrixSize];

    public int getMatrixSize(int matrixSize){
        int ms = matrixSize;
        return ms;
    }
    public void setMatrix(){
        for (int i = 0; i < matrixSize; i++ ){
           setLine(i);
        }
    }
    private void setLine(int lineNumber){
        for(int i = 0; i < matrixSize; i++){
            matrix[lineNumber][i] = (int)(Math.random()*10);
        }
    }

    public void setFreeMembers(){

        for(int i = 0; i < matrixSize; i++){
            freeMembers[i] = (int)(Math.random()*10);
        }
    }

    private void showLine(int lineNumber){
        for(int i = 0; i < matrixSize; i ++){
            System.out.print(matrix[lineNumber][i]+" ");

        }
    }

    public void showMatrix(){

        for (int i = 0; i < matrixSize; i++ ){
            System.out.println();
            showLine(i);
            System.out.print("|"+ freeMembers[i]);
            System.out.println();

        }

    }
    private void showLineL(int lineNumber){
        for(int i = 0; i < matrixSize; i ++){
            System.out.print(l[lineNumber][i]+" ");

        }
    }
    public void showL(){
        for (int i = 0; i < matrixSize; i++ ){
            System.out.println();
            showLineL(i);
            System.out.print("|"+ freeMembers[i]);
            System.out.println();

        }

    }

    private void firstStep(float[][] matrix, float[] freeMembers){

        for (int k = 0; k < matrixSize; k++){

            // finding max element
            int maxElement=k;
            maxElement=findingMax(maxElement, k);

            // swap row in matrix <matrix>
            swapLine(matrix,k,maxElement);

            //swap free members
            swapFreeMembers(freeMembers,k,maxElement);

            //step
            step(matrix,freeMembers,k,matrixSize);



        }

    }

    private void firstStepWithOutB(){
        for (int k = 0; k < matrixSize; k++){

            // finding max element
            int maxElement=k;
            maxElement=findingMax(maxElement, k);

            // swap row in matrix <matrix>
            swapLine(matrix,k,maxElement);

            //swap free members
            swapFreeMembers(freeMembers,k,maxElement);

            //step
            stepWihOutB(matrix,k,matrixSize);



        }

    }



    private void backStep(){

        for (int i = matrixSize - 1; i >= 0; i-- ){

            float sum = 0;
            for (int j = i + 1; j < matrixSize; j++){

                sum += matrix[i][j] * answers[j];
            }
            answers[i] = (freeMembers[i] - sum) / matrix[i][i];
        }

    }
    private void swapFreeMembers(float[] freeMembers, float[] answers){

        for (int i = 0; i < matrixSize; i++){

        }

    }

    private void step(float[][] matrix, float[] freeMembers, int k, int matrixSize){

        for (int i = k + 1; i < matrixSize; i++){

            float factor = matrix[i][k] / matrix[k][k];

            for (int j = k; j < matrixSize; j++){

                matrix[i][j] -= factor * matrix[k][j];
            }
            freeMembers[i] -= factor * freeMembers[k];

        }

    }

    private void stepWihOutB(float[][] matrix, int k, int matrixSize){
        for (int i = k + 1; i < matrixSize; i++){

            float factor = matrix[i][k] / matrix[k][k];
            l[k][k] = 1;
            l[i][k]=factor;
            
            for (int j = k; j < matrixSize; j++){

                matrix[i][j] -= factor * matrix[k][j];
            }


        }
    }

    private int findingMax(int maxElement, int k){
        for (int i = k + 1; i < matrixSize; i++){

            if (Math.abs(matrix[i][k]) > Math.abs(matrix[maxElement][k])){
                maxElement = i;
            }
        }
        return maxElement;
    }

    private void swapLine(float[][] matrix, int k, int maxElement){

        float[] temp = matrix[k];
        matrix[k] = matrix[maxElement];
        matrix[maxElement] = temp;

    }

    private void swapFreeMembers(float[] freeMembers, int k, int maxElement){
        float t = freeMembers[k];
        freeMembers[k] = freeMembers[maxElement];
        freeMembers[maxElement] = t;
    }

    private void showAnswers(){

        int countSolutions = answers.length;
        System.out.println("Answers:");
        for (int i = 0; i < countSolutions; i++){
            System.out.printf(" " + answers[i]);
        }
        System.out.println();

    }

    public void findSolutions(){

        firstStepWithOutB();
        firstStep(l,freeMembers);
        backStep();
        showAnswers();

    }



}
